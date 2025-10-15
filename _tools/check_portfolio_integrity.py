#!/usr/bin/env python3
"""
Portfolio integrity checks ( SoT = Source of Truth )

Adds:
  --create-missing-spec   If decision_dashboard_spec.md is missing, create a scaffold
  --run-pytest            Run pytest in the selected project and surface pass/fail
  --scan-core             Scan all projects under Core/** and summarize results
  (NEW) pyproject.toml    Verify core dependencies are pinned with ==
  (NEW) list_project.ps1  Verify it filters __pycache__ and .ipynb_checkpoints
"""

import argparse
import subprocess
import sys
from pathlib import Path

# ----- Repo-level expectations -----
REPO_TOOLS = [
    "_tools/nb_sanity_cell.py",
    "_tools/templates/model_card.md",
    "_tools/list_project.ps1",
]

# Core libs we want pinned (==) in pyproject.toml
CORE_DEPS = ["numpy", "pandas", "statsmodels", "scikit-learn", "matplotlib"]

# ----- Project-level expectations -----
REQUIRED_DIRS = ["data", "reports", "models", "src", "notebooks"]
REQUIRED_FILES = [
    "config.yaml",
    "model_card.md",
    "README.md",
    "notebooks/01_scm01_forecast_policy_sim.ipynb",
]
OPTIONAL_FILES = [
    "reports/decision_dashboard_spec.md",
]

REQUIRED_CONFIG_KEYS_AT_LEAST = [
    "project",
    "service_level_target",
    "lead_time_days",
    "review_period_days",
    "seed",
]

SANITY_MARKER = "# --- Sanity Check Cell (inline, self-contained) ---"


def ok(msg):
    print(f"  ✓ {msg}")


def warn(msg):
    print(f"  ~ {msg}")


def fail(msg):
    print(f"  ✗ {msg}")


def load_ipynb(path: Path):
    try:
        import json

        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        return {"_error": str(e)}


# ---------- New: pyproject.toml check ----------
def parse_pyproject_toml(path: Path):
    if not path.exists():
        return None
    try:
        try:
            import tomllib  # Python 3.11+
        except ImportError:
            import tomli as tomllib  # fallback
        return tomllib.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None


def collect_dependencies_from_pyproject(pp):
    """Support PEP 621 and Poetry layouts."""
    deps = {}

    # PEP 621: [project] dependencies = ["pkgA==1.2.3", ...]
    proj = pp.get("project", {})
    for spec in proj.get("dependencies", []) or []:
        # spec like "numpy==1.26.4" or "pandas>=2.2,<2.3"
        name = spec.split()[0]
        if "==" in name:
            pkg, ver = name.split("==", 1)
            deps[pkg.lower()] = f"=={ver}"
        else:
            # try to split on comparison operators
            parts = (
                name.replace(">=", " >= ")
                .replace("<=", " <= ")
                .replace("~=", " ~= ")
                .replace("==", " == ")
                .split()
            )
            pkg = parts[0]
            deps[pkg.lower()] = " ".join(parts[1:]) if len(parts) > 1 else ""
    # PEP 621 optional-dependencies (ignore for now)

    # Poetry: [tool.poetry.dependencies]
    tool = pp.get("tool", {})
    poetry = tool.get("poetry", {})
    poetry_deps = poetry.get("dependencies", {}) or {}
    for k, v in poetry_deps.items():
        if k.lower() == "python":  # skip python spec
            continue
        if isinstance(v, str):
            deps[k.lower()] = v
        elif isinstance(v, dict):
            # {version="==1.2.3", extras=[...]} etc.
            ver = v.get("version", "")
            deps[k.lower()] = ver
        else:
            deps[k.lower()] = ""

    return deps


def is_strict_pin(spec: str) -> bool:
    """Require exact pin ==X.Y.Z for core libs."""
    return spec.strip().startswith("==")


def check_pyproject_pins(root: Path, project_root: Path) -> bool:
    print("\n[ pyproject.toml dependency pins ]")
    # Look for pyproject.toml at project level; fall back to repo root
    pp = parse_pyproject_toml(project_root / "pyproject.toml")
    loc = project_root / "pyproject.toml"
    if pp is None:
        pp = parse_pyproject_toml(root / "pyproject.toml")
        loc = root / "pyproject.toml"

    if pp is None:
        warn("pyproject.toml not found — skipping pin check")
        return True

    deps = collect_dependencies_from_pyproject(pp)
    good = True
    for pkg in CORE_DEPS:
        spec = deps.get(pkg, "")
        if not spec:
            warn(f"{pkg} not declared")
            continue
        if is_strict_pin(spec):
            ok(f"{pkg} pinned ({spec})")
        else:
            fail(f"{pkg} not strictly pinned (spec: '{spec}'). Use '==x.y.z'")
            good = False
    return good


# ---------- New: list_project.ps1 filter check ----------
def check_list_project_filter(root: Path) -> bool:
    print("\n[ list_project.ps1 filter ]")
    path = root / "_tools" / "list_project.ps1"
    if not path.exists():
        warn("list_project.ps1 not found — skipping filter check")
        return True

    text = path.read_text(encoding="utf-8", errors="ignore")
    # Heuristics: ensure script filters out __pycache__ and .ipynb_checkpoints
    has_filter = (
        ("Where-Object" in text)
        and ("__pycache__" in text)
        and (".ipynb_checkpoints" in text)
    )
    if has_filter:
        ok("Filter present for __pycache__ and .ipynb_checkpoints")
        return True
    else:
        fail(
            "Filter missing — add Where-Object to exclude __pycache__ and .ipynb_checkpoints"
        )
        return False


# ---------- Existing checks ----------
def check_repo_tools(root: Path) -> bool:
    print("\n[ Repo-level tools/templates ]")
    good = True
    for rel in REPO_TOOLS:
        p = root / rel
        if p.exists():
            ok(f"{rel} found")
        else:
            fail(f"{rel} MISSING")
            good = False
    return good


def check_project_structure(project_root: Path, create_missing_spec: bool) -> bool:
    print(f"\n[ Project structure ] {project_root}")
    good = True
    for d in REQUIRED_DIRS:
        if (project_root / d).exists():
            ok(f"dir {d}/")
        else:
            fail(f"dir {d}/ MISSING")
            good = False
    for f in REQUIRED_FILES:
        if (project_root / f).exists():
            ok(f"file {f}")
        else:
            fail(f"file {f} MISSING")
            good = False

    for f in OPTIONAL_FILES:
        p = project_root / f
        if p.exists():
            ok(f"file {f}")
        else:
            warn(f"file {f} missing (optional)")
            if create_missing_spec and f.endswith("decision_dashboard_spec.md"):
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_text(DEFAULT_SPEC_MD, encoding="utf-8")
                ok(f"created {f}")
    return good


def check_config(project_root: Path) -> bool:
    print("\n[ config.yaml ]")
    import yaml

    cfg_path = project_root / "config.yaml"
    if not cfg_path.exists():
        fail("config.yaml not found")
        return False
    try:
        cfg = yaml.safe_load(cfg_path.read_text(encoding="utf-8"))
    except Exception as e:
        fail(f"config.yaml parse error: {e}")
        return False

    good = True
    missing = [k for k in REQUIRED_CONFIG_KEYS_AT_LEAST if k not in cfg]
    if missing:
        fail(f"missing keys: {missing}")
        good = False
    else:
        ok("required keys present")

    for k in ["data_dir", "reports_dir", "models_dir"]:
        if k in cfg:
            ok(f"{k} = {cfg[k]}")
        else:
            warn(f"{k} not set (optional)")

    return good


def check_sanity_cell(project_root: Path) -> bool:
    print("\n[ Sanity Check cell in entry notebook ]")
    nb_path = project_root / "notebooks/01_scm01_forecast_policy_sim.ipynb"
    if not nb_path.exists():
        fail("Entry notebook not found")
        return False

    nb = load_ipynb(nb_path)
    if "_error" in nb:
        fail(f"ipynb load error: {nb['_error']}")
        return False

    found = False
    for cell in nb.get("cells", []):
        if cell.get("cell_type") == "code":
            src = "".join(cell.get("source", []))
            if SANITY_MARKER in src:
                found = True
                break
    if found:
        ok("Sanity Check cell found (marker present)")
        return True
    else:
        fail("Sanity Check cell NOT found (marker missing)")
        return False


def run_pytest(project_root: Path) -> bool:
    print("\n[ Tests (pytest) ]")
    tests_dir = project_root / "tests"
    if not tests_dir.exists():
        warn("tests/ directory not found — skipping")
        return True
    cmd = ["pytest", "-q"]
    try:
        result = subprocess.run(
            cmd, cwd=str(project_root), capture_output=True, text=True
        )
        if result.stdout.strip():
            print(result.stdout.strip())
        if result.returncode == 0:
            ok("pytest passed")
            return True
        else:
            if result.stderr.strip():
                sys.stdout.write(result.stderr)
            fail(f"pytest failed (exit {result.returncode})")
            return False
    except FileNotFoundError:
        warn("pytest not found in PATH — skipping")
        return True


def check_single_project(
    root: Path, rel_project: str, create_missing_spec: bool, run_tests: bool
) -> bool:
    project_root = (root / rel_project).resolve()
    print("\n" + "=" * 70)
    print(f"Project: {project_root}")
    print("=" * 70)

    if not project_root.exists():
        fail("Project path not found")
        return False

    ok_tools = check_repo_tools(root)
    ok_list = check_list_project_filter(root)
    ok_struct = check_project_structure(project_root, create_missing_spec)
    ok_cfg = check_config(project_root)
    ok_cell = check_sanity_cell(project_root)
    ok_pins = check_pyproject_pins(root, project_root)
    ok_tests = run_pytest(project_root) if run_tests else True

    return all([ok_tools, ok_list, ok_struct, ok_cfg, ok_cell, ok_pins, ok_tests])


DEFAULT_SPEC_MD = """# Decision Dashboard — SCM-01

## 1) KPIs
- Forecast accuracy: sMAPE, MAPE
- Service level: achieved vs target (0.95)
- Inventory cost: holding, ordering, stockout
- Policy outcomes: (s,S) or (Q,R), backorders, fill rate

## 2) Views
- Exec Summary (KPI tiles + traffic lights)
- Forecast vs Actual (time series + error bands)
- Inventory Trajectory (on-hand, pipeline, reorder points)
- Sensitivity Panel (lead time, service target, cost rates)

## 3) Controls
- Scenario selector (baseline vs candidate)
- Policy parameters (R/Q or s/S)
- Demand variance multiplier

## 4) Data contracts
- Input: data/processed/demand_weekly.parquet
- Config: config.yaml (lead_time_days, service_level_target, costs)
- Output: reports/figures/*.png + models/* (optional)

## 5) Governance
- Seed + git commit printed by the Sanity Cell
- Config SHA shown on dashboard footer
"""


def find_core_projects(root: Path):
    core = root / "Core"
    if not core.exists():
        return []
    projects = []
    for p in core.rglob("*"):
        if p.is_dir() and (p / "notebooks").exists() and (p / "config.yaml").exists():
            projects.append(str(p.relative_to(root)))
    return sorted(set(projects))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".", help="Path to Portfolio root")
    ap.add_argument(
        "--project",
        default="Core/Supply_Chain_Logistics/SCM-01_forecasting_inventory_policies",
        help="Relative path from root to a project folder",
    )
    ap.add_argument(
        "--create-missing-spec",
        action="store_true",
        help="Create decision_dashboard_spec.md if missing",
    )
    ap.add_argument(
        "--run-pytest",
        action="store_true",
        help="Run pytest in the project and report result",
    )
    ap.add_argument(
        "--scan-core",
        action="store_true",
        help="Scan all Core/** projects instead of a single project",
    )
    args = ap.parse_args()

    root = Path(args.root).resolve()

    print("===== PORTFOLIO INTEGRITY CHECK =====")
    print(f"Root:    {root}")

    all_good = True
    if args.scan_core:
        projects = find_core_projects(root)
        if not projects:
            fail("No projects found under Core/**")
            sys.exit(1)
        print(f"Found {len(projects)} project(s).")
        results = []
        for rel in projects:
            good = check_single_project(
                root, rel, args.create_missing_spec, args.run_pytest
            )
            results.append((rel, good))
            all_good &= good

        print("\n===== SUMMARY =====")
        for rel, good in results:
            print(f"{'✅ PASS' if good else '❌ FAIL'} — {rel}")
    else:
        print(f"Project: {(root / args.project).resolve()}")
        all_good &= check_single_project(
            root, args.project, args.create_missing_spec, args.run_pytest
        )

    print("\n===== RESULT =====")
    if all_good:
        print("✅ PASS — Structure and standards look good.")
        sys.exit(0)
    else:
        print("❌ FAIL — See issues above.")
        sys.exit(1)


if __name__ == "__main__":
    main()
