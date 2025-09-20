"""
FastAPI verification microservice.
Reads the local anchor registry and verifies whether a hash (and optional ref) exists.

Run:
  uvicorn services.verify_api.main:app --reload

Example:
  curl "http://127.0.0.1:8000/verify?hash=<hex>&ref=local://..."
"""
from fastapi import FastAPI, Query
from pydantic import BaseModel
from pathlib import Path
import json

app = FastAPI(title="Anchor Verify API", version="0.1.0")

REGISTRY_PATH = Path("Blockchain/common/utils/_local_anchor_registry.json")

class VerifyResponse(BaseModel):
    ok: bool
    hash: str
    ref: str | None = None
    reason: str | None = None

def load_registry():
    if REGISTRY_PATH.exists():
        return json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    return {}

@app.get("/healthz")
def healthz():
    return {"status": "ok", "registry_exists": REGISTRY_PATH.exists()}

@app.get("/verify", response_model=VerifyResponse)
def verify(hash: str = Query(..., description="Hex SHA-256 digest"),
           ref: str | None = Query(None, description="Optional reference string to match")):
    if not hash or len(hash) != 64:
        return VerifyResponse(ok=False, hash=hash, ref=ref, reason="invalid hash length")
    reg = load_registry()
    entry = reg.get(hash)
    if not entry:
        return VerifyResponse(ok=False, hash=hash, ref=ref, reason="hash not found")
    if ref is not None and entry.get("ref") != ref:
        return VerifyResponse(ok=False, hash=hash, ref=ref, reason="ref mismatch")
    return VerifyResponse(ok=True, hash=hash, ref=ref)
