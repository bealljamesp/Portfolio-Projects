# src/bootstrap.py
from __future__ import annotations
from pathlib import Path
import os
from typing import Any, Dict

try:
    import yaml  # PyYAML
except ModuleNotFoundError:
    raise ModuleNotFoundError(
        "PyYAML is required. Install with:\n  conda install pyyaml  OR  pip install pyyaml"
    )


def load_config(project_root: Path) -> Dict[str, Any]:
    cfg_path = project_root / "config.yaml"
    if cfg_path.exists():
        with open(cfg_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f) or {}
    print("⚠️  config.yaml not found — using defaults")
    return {}


def init_project() -> Dict[str, Any]:
    """
    Initializes notebook/project environment:
    - Sets CWD to project root (handles launching from /notebooks)
    - Ensures data/report dirs exist
    - Loads config.yaml (if present)
    Returns a dict with handy paths and config.
    """
    # Detect project root
    project_root = Path.cwd()
    if project_root.name.lower() == "notebooks":
        project_root = project_root.parent
        os.chdir(project_root)

    # Paths
    DATA_DIR = project_root / "data"
    RAW_DIR = DATA_DIR / "raw"
    INTERIM_DIR = DATA_DIR / "interim"
    PROCESSED_DIR = DATA_DIR / "processed"
    FIG_DIR = project_root / "reports" / "figures"

    for p in (RAW_DIR, INTERIM_DIR, PROCESSED_DIR, FIG_DIR):
        p.mkdir(parents=True, exist_ok=True)

    # Config
    CONFIG = load_config(project_root)
    SEED = CONFIG.get("seed", 42)

    # Friendly print
    print(f"Project Root: {project_root}")
    print(f"Data        : {DATA_DIR}")
    print(f"Figures     : {FIG_DIR}")
    print(
        f"Config      : {'config.yaml' if (project_root/'config.yaml').exists() else 'None'}"
    )
    return {
        "PROJECT_ROOT": project_root,
        "DATA_DIR": DATA_DIR,
        "RAW_DIR": RAW_DIR,
        "INTERIM_DIR": INTERIM_DIR,
        "PROCESSED_DIR": PROCESSED_DIR,
        "FIG_DIR": FIG_DIR,
        "CONFIG": CONFIG,
        "SEED": SEED,
    }
