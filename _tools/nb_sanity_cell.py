# --- Sanity Check Cell (inline, self-contained) ---
import hashlib
import json
import os
import platform
import subprocess
import sys
from datetime import datetime
from pathlib import Path


def _try_import(name):
    try:
        mod = __import__(name)
        return mod, getattr(mod, "__version__", "unknown")
    except Exception as e:
        return None, f"NOT AVAILABLE ({e})"


def _sha256(path):
    try:
        h = hashlib.sha256()
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(65536), b""):
                h.update(chunk)
        return h.hexdigest()[:16]
    except Exception:
        return None


def _git_info():
    try:
        commit = (
            subprocess.check_output(
                ["git", "rev-parse", "--short", "HEAD"], stderr=subprocess.DEVNULL
            )
            .decode()
            .strip()
        )
    except Exception:
        commit = None
    try:
        dirty = (
            subprocess.check_output(
                ["git", "status", "--porcelain"], stderr=subprocess.DEVNULL
            )
            .decode()
            .strip()
        )
        dirty = bool(dirty)
    except Exception:
        dirty = None
    return {"commit": commit, "dirty": dirty}


RUN_TS = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
ROOT = Path.cwd()
DATA = ROOT / "data"
CONFIG = ROOT / "config.yaml"

mods = {}
for m in [
    "numpy",
    "pandas",
    "matplotlib",
    "scipy",
    "sklearn",
    "statsmodels",
    "seaborn",
]:
    mod, ver = _try_import(m)
    mods[m] = ver

env_info = {
    "python": sys.version.split()[0],
    "platform": platform.platform(),
    "conda_env": os.environ.get("CONDA_DEFAULT_ENV"),
}

paths = {
    "root_exists": ROOT.exists(),
    "data_exists": DATA.exists(),
    "config_exists": CONFIG.exists(),
    "config_sha256_16": _sha256(CONFIG) if CONFIG.exists() else None,
}

git = _git_info()

report = {
    "run_timestamp": RUN_TS,
    "env": env_info,
    "modules": mods,
    "paths": paths,
    "git": git,
}

print(json.dumps(report, indent=2))

# Assertions (adjust to your needs)
assert paths["data_exists"], "Expected ./data directory to exist"
if paths["config_exists"]:
    print("config.yaml detected ✓")
else:
    print("WARNING: config.yaml not found — using defaults")

# Set global, deterministic seed if needed
try:
    import random as _rnd

    import numpy as _np

    _np.random.seed(42)
    _rnd.seed(42)
except Exception:
    pass
# --- End Sanity Check Cell ---
