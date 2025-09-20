# Verify API (FastAPI)

A tiny verification service that checks your local anchor registry.

## Run

From your Portfolio root (where `Blockchain/common/utils/_local_anchor_registry.json` lives):

```bash
uvicorn services.verify_api.main:app --reload
```

## Endpoints

- `GET /healthz` – basic health check.
- `GET /verify?hash=<hex>[&ref=...]` – returns JSON `{ ok: true|false, ... }`.

## Notes

- This reads your **local** registry file created by `hash_anchor.py`.
- Later, you can swap the registry lookups to call a blockchain node instead.
