import requests
from urllib.parse import quote
from pathlib import Path
import json

def verify_local(hex_hash: str, ref: str | None = None, base: str = "http://127.0.0.1:8000", strict: bool = True) -> dict:
    """Call the local Verify API. If strict=False, the server ignores ref mismatches (if supported)."""
    params = {"hash": hex_hash}
    if ref is not None:
        params["ref"] = ref  # requests will encode '#' in params
    if not strict:
        params["strict"] = "false"
    r = requests.get(f"{base}/verify", params=params, timeout=8)
    r.raise_for_status()
    return r.json()

def get_dataset_hash_from_manifest(manifest_path: str | Path) -> str:
    m = json.loads(Path(manifest_path).read_text(encoding="utf-8"))
    return m["dataset_hash"]

def verify_auto_from_manifest(manifest_path: str | Path,
                              preferred_ref: str,
                              base: str = "http://127.0.0.1:8000",
                              strict: bool = True) -> dict:
    """Loads hash, tries preferred ref; if that fails and strict=True, retries without ref."""
    h = get_dataset_hash_from_manifest(manifest_path)
    resp = verify_local(h, preferred_ref, base=base, strict=strict)
    if not resp.get("ok") and strict:
        # existence-only fallback
        return verify_local(h, None, base=base, strict=strict)
    return resp
