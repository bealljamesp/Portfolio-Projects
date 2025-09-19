"""
hash_anchor.py
Minimal helper to hash rows/files and register their digest in a local JSON registry.
This simulates a blockchain "anchor" so you can learn the workflow before using web3.py.
"""
from __future__ import annotations
import hashlib, json, time
from pathlib import Path
from typing import Dict

REGISTRY_PATH = Path("Blockchain/common/utils/_local_anchor_registry.json")

def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def sha256_file(path: str | Path) -> str:
    p = Path(path)
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

def _load_registry() -> Dict[str, dict]:
    if REGISTRY_PATH.exists():
        return json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    return {}

def _save_registry(reg: Dict[str, dict]) -> None:
    REGISTRY_PATH.parent.mkdir(parents=True, exist_ok=True)
    REGISTRY_PATH.write_text(json.dumps(reg, indent=2), encoding="utf-8")

def anchor_hash(hex_digest: str, ref: str) -> None:
    reg = _load_registry()
    if hex_digest in reg:
        raise ValueError("Hash already anchored")
    reg[hex_digest] = {"ref": ref, "ts": int(time.time())}
    _save_registry(reg)

def verify_hash(hex_digest: str, ref: str | None = None) -> bool:
    reg = _load_registry()
    if hex_digest not in reg:
        return False
    return (ref is None) or (reg[hex_digest]["ref"] == ref)

if __name__ == "__main__":
    # Example: hash this file and anchor it
    digest = sha256_file(__file__)
    anchor_hash(digest, ref="local://hash_anchor.py")
    print("Anchored:", digest)
    print("Verify:", verify_hash(digest, "local://hash_anchor.py"))
