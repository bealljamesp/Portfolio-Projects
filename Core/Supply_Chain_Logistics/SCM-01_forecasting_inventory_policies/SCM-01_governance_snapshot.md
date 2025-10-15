# 🗂️ SCM-01 Governance Snapshot

**Project:** Forecasting & Inventory Policies  
**Code:** SCM-01_forecasting_inventory_policies  
**Phase:** Decision Foundations  
**Snapshot Date:** 2025-10-14  
**Governance Version:** Decision Foundations v1.0 Standards  

---

## 📘 Purpose
Record the active governance framework, policies, and standards in place at the time SCM-01 was launched.  
This snapshot provides traceability for how portfolio-level standards evolve between projects.

---

## 📁 Active Governance Documents

| Document | Location | Description |
|-----------|-----------|-------------|
| `SCM-01_Project_Overview.md` | Project root | Defines scenario, objectives, and analytical plan. |
| `SCM-01_lessons_log.md` | Project root | Records in-project insights and “wish I had known” lessons. |
| `SCM-01_handoff_todo.md` | Project root | Tracks pending governance updates for Central. |
| `central_handoff_standards.md` | Portfolio/docs/handoff | Official rulebook for project → central handoff process. |
| `lessons_learned_log.md` | Portfolio/docs | Portfolio-wide record of finalized lessons. |
| `manual_project_creation_checklist.md` | Portfolio/docs | Step-by-step procedure for new projects. |
| `portfolio_project_guidance.md` | Portfolio/docs | Defines philosophy, tone, and technical quality standards. |

---

## ⚙️ Active Standards and Policies (as of 2025-10-14)

| Area | Standard |
|------|-----------|
| **File Naming Convention** | `{CODE}_{descriptor}.md` (e.g., `SCM-01_Project_Overview.md`) |
| **Project Lifecycle** | Kickoff → Development → Governance Review → Handoff |
| **Documentation Format** | Long outputs provided as downloadable files to minimize DOM load |
| **Lessons Logging** | Project-level log + portfolio-level consolidation |
| **Verification Policy** | PowerShell file check confirms all governance docs exist in correct folders |
| **Central Duties** | Integrate lessons, update templates, maintain dashboard |
| **Reproducibility** | Config-driven workflow with seed and pinned dependencies |
| **Integrity Validation** | `_tools/check_portfolio_integrity.py` confirms structure and pins |

---

## 🧩 Verification Summary (PowerShell Check)

**Status:** ✅ Passed  
**Timestamp:** 2025-10-14  
**Confirmed Files:**  
- SCM-01_Project_Overview.md  
- SCM-01_lessons_log.md  
- SCM-01_handoff_todo.md  
- central_handoff_standards.md  

Result: All governance documents verified and correctly placed.

---

## 🧭 Next Governance Improvements (from SCM-01_handoff_todo.md)

| Improvement | Target Document | Status |
|--------------|-----------------|---------|
| Add Governance Stage Summary cell | portfolio_project_guidance.md | Pending |
| Add project_manifest.json template | manual_project_creation_checklist.md | Pending |
| Create central_dashboard.md | Portfolio/docs/ | Pending |
| Add README Reflections section | README templates | Pending |
| Add Experimental Sandbox tag | Guidance + checklists | Pending |

---

## 🧠 Notes for Central Workspace
- This snapshot represents the *baseline governance model* used to initialize SCM-01.  
- Upon SCM-01 completion, Central should archive this file (read-only) and create a diff log showing changes in portfolio standards before SCM-02 initialization.

---

**Author:** Portfolio Governance System  
**Maintainer:** Central Workspace (Decision Foundations Layer)  
**Version:** 1.0  
**Last Updated:** 2025-10-14  

---
