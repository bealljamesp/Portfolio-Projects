from pathlib import Path

import yaml

CFG_FILE = Path("config.yaml")
REQUIRED_KEYS = [
    "project",
    "data_dir",
    "reports_dir",
    "models_dir",
    "holding_cost_rate",
    "service_level_target",
]


def test_config_exists():
    assert CFG_FILE.exists(), "Missing config.yaml"


def test_config_keys():
    cfg = yaml.safe_load(open(CFG_FILE))
    missing = [k for k in REQUIRED_KEYS if k not in cfg]
    assert not missing, f"Missing keys: {missing}"


def test_core_paths_exist():
    for d in ["data", "reports", "src", "notebooks", "models"]:
        assert Path(d).exists(), f"Expected {d}/ directory"
