# 🧭 Central Workspace 002 – Portfolio State Snapshot (Pre-SCM-01 Execution)

## 🔹 Purpose  
Establish portfolio-level structure, governance scaffolding, and manual project creation workflow before entering the detailed SCM-01 build phase.  
This chat focused on strengthening reproducibility, organization, and knowledge continuity across projects.

---

## 🗂️ Directory & File Updates

### **1. Portfolio/docs/**
| File | Purpose | Status |
|------|----------|--------|
| `project_gameplan.md` | Defines the **strategic roadmap** for all portfolio phases (Decision Foundations → Governance & Trust). | ✅ Verified and referenced for DA/SCM project planning. |
| `manual_project_creation_checklist.md` | Step-by-step guide for **manual project setup and validation**, designed for learning and reproducibility. | ✅ Created in this chat. |
| `lessons_learned_log.md` | Template for **recording insights and handoffs** between projects (Lessons Learned – SCM-01, etc.). | ✅ Created in this chat. |
| `README.md` | Overview of documentation structure and governance principles. | ✅ Created in this chat for folder clarity. |

> Together, these form your lightweight **Portfolio Governance Layer** (strategy + process + reflection).

---

### **2. Portfolio/_tools/**
| File | Purpose | Status |
|------|----------|--------|
| `_tools/check_portfolio_integrity.py` | Enhanced to include: <br>• `pyproject.toml` strict pin check<br>• `_tools/list_project.ps1` filter validation | ✅ Updated in this chat. |
| `_tools/check_portfolio.ps1` | PowerShell wrapper for running the integrity check. | ✅ Updated and verified. |
| `_tools/templates/pyproject_portfolio.toml` | Template for future projects with pinned dependencies and Ruff config. | ✅ Created in this chat. |

> These ensure portfolio-wide **reproducibility contracts** and consistent validation tools.

---

### **3. Portfolio/Core/Supply_Chain_Logistics/SCM-01_forecasting_inventory_policies/**
| File | Purpose | Status |
|------|----------|--------|
| `pyproject.toml` | Strictly pinned dependencies (`numpy==1.26.4`, etc.) + Ruff config. | ✅ Verified. |
| `config.yaml` | Updated with standard keys (`data_dir`, `reports_dir`, `models_dir`). | ✅ Verified. |
| `notebooks/01_scm01_forecast_policy_sim.ipynb` | Sanity Check Cell inserted and validated via integrity check. | ✅ Verified. |
| `reports/decision_dashboard_spec.md` | Added under `/reports/figures/` and detected by integrity check. | ✅ Verified. |
| `tests/test_config.py` | Basic pytest validation implemented. | ✅ Verified (3 passed tests). |
| `models/` | Created (empty) for reproducible model artifacts. | ✅ Created. |
| `.vscode/`, `src/`, `data/`, `reports/` | Structure confirmed via list_project.ps1 (no duplicates, clean tree). | ✅ Verified. |

> SCM-01 is now your **portfolio baseline project** — it defines the template for all future builds.

---

### **4. Portfolio/_tools/list_project.ps1**
- Refactored for **clean output formatting**, color-coded folder/file display, and indentation.  
- Now hides `__pycache__` and `.ipynb_checkpoints` directories automatically.  
✅ Verified via latest integrity check.

---

## 🧩 Concepts Strengthened

| Concept | Description | Artifacts Implementing It |
|----------|--------------|---------------------------|
| **Reproducibility Contracts** | Guarantees consistent results under same environment and data. | `pyproject.toml`, `config.yaml`, Sanity Cell, integrity checker. |
| **Governance (Intro Level)** | Ensures traceability and explainability at project and portfolio levels. | `model_card.md`, `decision_dashboard_spec.md`, `lessons_learned_log.md`. |
| **SoT (Source of Truth)** | Data stored once, under `/data/`, no redundant copies. | Confirmed via structure audit. |
| **Manual Learning Cycle** | Focus on deliberate, non-automated project creation for deeper understanding. | `manual_project_creation_checklist.md`. |
| **Integrity + Pytest Dual-Layer Validation** | Structural audit (static) + logic validation (dynamic). | `check_portfolio_integrity.py` with `--run-pytest`. |

---

## 🧠 Active Knowledge / Next Actions

1. **SCM-01 Chat (Active Execution Phase)**  
   - Use the SCM-01 launch prompt already passed.  
   - Follow the Forecast → Policy → Simulation → Decision architecture.  
   - Maintain self-contained, explainable results.

2. **Return Here (Central Workspace)**  
   - When SCM-01 is complete, summarize insights using:
     ```markdown
     ### Lessons Learned – SCM-01
     ```
     inside `docs/lessons_learned_log.md`.
   - Review reproducibility, process, and governance notes.  
   - Adjust checklist if any steps need refinement before DA-01.

3. **Next Project: DA-01 Churn Prediction (Logit)**  
   - Start from the `manual_project_creation_checklist.md`.  
   - Copy SCM-01 structure, adapt for DA domain.  
   - Use the DA-01 chat starter prompt already drafted.  

4. **Future Governance Module (after SCM-01)**  
   - Revisit portfolio-level governance theory and how it ties to explainability, traceability, and ethical AI.  
   - Integrate governance maturity concepts into the docs layer.

---

### ✅ Portfolio Status Summary
| Layer | Status |
|--------|--------|
| **Docs Layer** | Complete — roadmap, checklist, lessons log, and README ready. |
| **Tools Layer** | Fully functional — integrity + pytest validation, SoT confirmed. |
| **Baseline Project (SCM-01)** | Verified — structure, config, pins, and tests all passing. |
| **Next Step** | Execute SCM-01 workflow; capture lessons learned on completion. |

---
