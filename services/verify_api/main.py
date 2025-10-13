"""
Anchor Verify API
- Local registry mode (default)
- On-chain mode (set VERIFY_MODE=onchain) using web3.py

Env (for on-chain):
  VERIFY_MODE=onchain
  RPC_URL=...
  CONTRACT_ADDRESS=0x...
Optional query params:
  strict=false   -> ignore ref mismatch (existence-only)
"""
from fastapi import FastAPI, Query
from pydantic import BaseModel
from pathlib import Path
from typing import Optional
import os, json

try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    pass

app = FastAPI(title="Anchor Verify API", version="0.2.0")

REGISTRY_PATH = Path("Blockchain/common/utils/_local_anchor_registry.json")

class VerifyResponse(BaseModel):
    ok: bool
    hash: str
    ref: Optional[str] = None
    reason: Optional[str] = None
    mode: str

def load_registry():
    if REGISTRY_PATH.exists():
        return json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    return {}

# ---------- Local verifiers ----------

def verify_local(hash_hex: str, ref: Optional[str], strict: bool) -> VerifyResponse:
    reg = load_registry()
    entry = reg.get(hash_hex)
    if not entry:
        return VerifyResponse(ok=False, hash=hash_hex, ref=ref, reason="hash not found", mode="local")
    if not strict:
        return VerifyResponse(ok=True, hash=hash_hex, ref=ref, reason=None, mode="local")
    if ref is not None and entry.get("ref") != ref:
        return VerifyResponse(ok=False, hash=hash_hex, ref=ref, reason="ref mismatch", mode="local")
    return VerifyResponse(ok=True, hash=hash_hex, ref=ref, reason=None, mode="local")

# ---------- On-chain verifiers ----------

_w3 = None
_contract = None
_abi_cache = None

def get_web3_contract():
    global _w3, _contract, _abi_cache
    if _contract is not None:
        return _contract
    from web3 import Web3
    rpc = os.getenv("RPC_URL")
    addr = os.getenv("CONTRACT_ADDRESS")
    if not rpc or not addr:
        raise RuntimeError("RPC_URL and CONTRACT_ADDRESS must be set for VERIFY_MODE=onchain")
    abi_path = Path("services/web3_anchor/ProofOfProvenance.abi.json")
    if not abi_path.exists():
        raise RuntimeError("ABI file not found at services/web3_anchor/ProofOfProvenance.abi.json")
    _abi_cache = json.loads(abi_path.read_text(encoding="utf-8"))
    _w3 = Web3(Web3.HTTPProvider(rpc))
    _contract = _w3.eth.contract(address=Web3.to_checksum_address(addr), abi=_abi_cache)
    return _contract

def verify_onchain(hash_hex: str, ref: Optional[str], strict: bool):
    if len(hash_hex) != 64:
        return {"ok": False, "hash": hash_hex, "ref": ref, "reason": "invalid hash length", "mode": "onchain"}
    try:
        c = get_web3_contract()
        hbytes = bytes.fromhex(hash_hex)
        exists = bool(c.functions.exists(hbytes).call())
        if not exists:
            return {"ok": False, "hash": hash_hex, "ref": ref, "reason": "hash not found", "mode": "onchain"}
        if not strict or ref is None:
            return {"ok": True, "hash": hash_hex, "ref": ref, "reason": None, "mode": "onchain"}
        # Try to fetch stored ref (supports either getReference or reference)
        stored_ok = None
        stored_ref = None
        try:
            stored_ok, stored_ref = c.functions.getReference(hbytes).call()
        except Exception:
            try:
                stored_ref = c.functions.reference(hbytes).call()
                stored_ok = stored_ref is not None
            except Exception:
                stored_ok = False
        if not stored_ok:
            # If chain doesn't store ref, treat existence as success in strict mode
            return {"ok": True, "hash": hash_hex, "ref": ref, "reason": None, "mode": "onchain"}
        if stored_ref != ref:
            return {"ok": False, "hash": hash_hex, "ref": ref, "reason": "ref mismatch", "mode": "onchain"}
        return {"ok": True, "hash": hash_hex, "ref": ref, "reason": None, "mode": "onchain"}
    except Exception as e:
        return {"ok": False, "hash": hash_hex, "ref": ref, "reason": f"onchain error: {e}", "mode": "onchain"}

@app.get("/healthz")
def healthz():
    mode = os.getenv("VERIFY_MODE", "local").lower()
    out = {"status": "ok", "mode": mode, "registry_exists": REGISTRY_PATH.exists()}
    if mode == "onchain":
        out["has_rpc"] = bool(os.getenv("RPC_URL"))
        out["has_contract"] = bool(os.getenv("CONTRACT_ADDRESS"))
    return out

@app.get("/verify")
def verify(
    hash: str,
    ref: Optional[str] = None,
    strict: bool = True
):
    mode = os.getenv("VERIFY_MODE", "local").lower()
    if mode == "onchain":
        return verify_onchain(hash, ref, strict)
    else:
        # basic validation like before
        if not hash or len(hash) != 64:
            return {"ok": False, "hash": hash, "ref": ref, "reason": "invalid hash length", "mode": "local"}
        return verify_local(hash, ref, strict).__dict__
