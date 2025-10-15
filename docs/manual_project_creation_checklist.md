# 🧭 Manual Project Creation Checklist (Portfolio Learning Mode)

**Purpose:**
Build the next portfolio project *manually* to strengthen understanding of each moving part — structure, configuration, reproducibility, governance, and validation.
This mirrors how professional data-science systems are built before automation layers are added.

---

## ⚙️ Quick Reference Commands

| Action | Command |
|--------|----------|
| Run integrity check | `python _tools/check_portfolio_integrity.py` |
| Run full check with tests | `python _tools/check_portfolio_integrity.py --run-pytest` |
| List directory structure | `powershell ./_tools/list_project.ps1 -Path <project_path>` |
| Run tests directly | `pytest -q` |
| Insert sanity cell into notebook | `powershell ./_tools/init_notebook.ps1 -NotebookPath <path> -SanityCellPath ./_tools/nb_sanity_cell.py` |

---

## 🔹 Phase 1 – Copy & Initialize

1. **Clone SCM-01**
   - Duplicate the entire `SCM-01_forecasting_inventory_policies` folder.
   - Rename using: `SCM-02_network_optimization_montecarlo` (or appropriate name).
   - Delete project-specific data in `data/` (keep folder structure).

2. **Update Core Files**
   - `README.md` → new title and project summary.
   - `config.yaml` → update parameters (costs, service levels, etc.).
   - `model_card.md` → replace use case, data description, and metrics.
   - `pyproject.toml` → keep dependencies, update metadata (`name`, `description`).

3. **Run integrity check**
   ```powershell
   python _tools/check_portfolio_integrity.py
   ```
   Use output feedback to fix missing or misconfigured elements until it passes.

---

## 🔹 Phase 2 – Sanity Check Cell & Environment

1. Open `notebooks/01_<project_name>_main.ipynb`.
2. Confirm the first cell contains the **Sanity Check Cell** marker:
   `# --- Sanity Check Cell (inline, self-contained) ---`
3. Modify one small part (e.g., add an extra check for file encoding).
4. Re-run the notebook and compare JSON output — note how environment details are logged.

---

## 🔹 Phase 3 – Functional Testing

1. Create a new test file under `tests/`:
   ```python
   def test_config_loads():
       import yaml
       cfg = yaml.safe_load(open("config.yaml"))
       assert "project" in cfg
   ```
2. Run:
   ```powershell
   pytest -q
   ```
3. Intentionally break something (rename a key) and re-run pytest to observe error reporting.
   Fix and rerun until tests pass.

---

## 🔹 Phase 4 – Decision Dashboard Spec

1. Create `reports/decision_dashboard_spec.md`.
2. Define: KPIs, visuals, and data sources.
3. Save one placeholder figure to `reports/figures/` and confirm it appears in the directory listing.

---

## 🔹 Phase 5 – Version & Reproducibility Drill

1. Change one dependency pin in `pyproject.toml` (e.g., `numpy==1.26.4` → `numpy>=1.26`) and rerun integrity check.
2. Observe failure messages — see how the checker enforces strict pins.
3. Revert the change and re-run to confirm the fix.

---

## 🔹 Phase 6 – Governance & Reflection

1. Ensure `model_card.md` and `decision_dashboard_spec.md` include:
   - Purpose
   - Data inputs
   - Methods & assumptions
   - Evaluation metrics
   - Governance / versioning notes

2. Add a reflection to `notes.md`:
   > “What I learned building SCM-02 manually — what went wrong, what I fixed, what I understand better now.”

3. Final validation:
   ```powershell
   python _tools/check_portfolio_integrity.py --run-pytest
   ```
   Passing means **portfolio-compliant and reproducible.**

---

## 💬 Chat Prompt for New Project Setup

> **Prompt:**
> “Continue from the manual project creation checklist.
> We’re building the next project manually (no automation) to reinforce reproducibility, governance, and testing concepts.
> The base reference is SCM-01.
> Help me walk through each step — copy, reconfigure, sanity-check, test, and validate with the integrity script.”

**Process Lessons:**
- Added PowerShell verification script to confirm file integrity and location at both project and central levels.
- Standardized governance file naming and handoff workflow; confirmed reproducibility.
