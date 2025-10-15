# 🧭 Central Workspace v3 — Active Overview
**Date:** 2025-10-15 05:06  
**Version:** v3  
**Location:** `Portfolio/docs/handoff/`

---

## 🎯 Purpose
This file anchors the **active coordination workspace** for the analytics portfolio.  
It provides current portfolio structure, project status, governance topics, and instructions for project handoffs.  
Use it to synchronize all project chats, maintain continuity, and launch new projects with full context.

---

## 📂 Portfolio Overview

### Core Domains
- **Data_Analytics**
  - DA-01_churn_prediction_logit
  - DA-02_time_series_forecasting
- **Finance**
- **HR_People_Analytics**
- **Supply_Chain_Logistics**
  - SCM-01_forecasting_inventory_policies
  - SCM-02_network_optimization_montecarlo

### Enablers
- **Governance_Layer**
  - Blockchain → BLK-01_pharma_serialization_dscsa_sim, common
  - Ethical_AI_Policy, Generative_Support, Human_AI_Collaboration, Responsible_AI → GOV-01_responsible-ai-dashboard
- **Intelligence_Layer**
  - AI_Assisted_Analytics → _Legacy_AI, AI-01_ai_forecasting_retail_demand, AI-02_generativeai_supplychaindocs
  - Causal_Graphs, Explainable_AI, Optimization_RL
- **System_Layer**
  - Edge_IoT → IOT-01_predictive-maintenance-demo
  - Knowledge_Graphs → KG-01_logistics-knowledge-graph
  - Sim_Opt_Hybrids, Simulation_Digital_Twins

### Documentation
Located in `Portfolio/docs/`  
`glossary.md`, `lessons_learned_log.md`, `manual_project_creation_checklist.md`,  
`next_generation_enablers.md`, `portfolio_init.log`, `portfolio_project_guidance.md`,  
`project_gameplan.md`, `project_skills_summary.txt`

---

## 📘 Reference Documents (Do Not Duplicate in Handoffs)
| File | Purpose | Location |
|------|----------|-----------|
| `portfolio_project_guidance.md` | Defines portfolio tone, standards, and QA gates | `/docs/` |
| `project_gameplan.md` | Outlines project sequence and learning goals | `/docs/` |
| `next_generation_enablers.md` | Explains Decision Intelligence and modern enablers | `/docs/` |
| `manual_project_creation_checklist.md` | Project initialization process | `/docs/` |

> These remain canonical in `/docs` and are **attached (not copied)** when handing off to new project chats.

---

## 🧩 Coordination Rules
- **Central Workspace (this)** = coordination, governance, and version control.  
- **Project Chats** = execution (each has its own reasoning and deliverables).  
- **Handoff Docs** (`/docs/handoff/`) = snapshots used to launch new projects.  
- **Snapshots** (`/docs/snapshots/`) = frozen context for archival or rollback.  

Update this file whenever:
1. A project finishes (add lessons & create `handoff_<from>_to_<to>.md`)
2. Standards change (update `guidance` or `gameplan`)
3. A new project starts (bump version to v4, v5, etc.)

---

## 📊 Project Dashboard (as of v3)

| Project | Domain | Status | Next Step |
|----------|---------|---------|------------|
| SCM-01_forecasting_inventory_policies | Supply Chain | 🟢 Active | Build baseline forecasting → inventory → simulation → decision flow |
| DA-01_churn_prediction_logit | Data Analytics | ⚪ Queued | Scaffold repo; follow SCM-01 standards |
| DA-02_time_series_forecasting | Data Analytics | ⚪ Planned | To follow DA-01 |
| SCM-02_network_optimization_montecarlo | Supply Chain | ⚪ Planned | Launch after SCM-01 lessons integrated |
| AI-01_ai_forecasting_retail_demand | Intelligence Layer | ⚪ Planned | Introduce AI-assisted analytics |
| GOV-01_responsible-ai-dashboard | Governance Layer | ⚪ Planned | Build after AI-01 & DA-02 complete |

---

## 🧱 Ongoing Governance / Topic Log

### Governance & Integration Layer
- How should Data, AI, and Project Governance connect within the same framework?  
- Central vs. distributed Responsible AI metadata (`governance.yaml` schema idea).  
- Minimum governance fields for every repo (`data_provenance`, `model_card`, `ethics_notes`).  
- Cadence for governance reviews (per milestone or per release?).  
- Mechanisms for simulation & analytics outputs to feed Responsible AI dashboards automatically.

### Cross-Project & Portfolio
- Propagating improvements from SCM-01 into new projects.  
- Versioning shared tools to avoid breaking dependencies.  
- Organizing cross-domain analytics (SCM + Finance).  

### Documentation & Learning
- Standardize format for `lessons_learned_log.md` entries.  
- Add “governance insight” section to the lessons log.  
- Expand `next_generation_enablers.md` as new enablers emerge.

---

## 🪄 Handoff Kit Instructions (for Launching a New Project)

When starting a new project (e.g., SCM‑01, DA‑01, AI‑01), attach **all** of the following files to the new chat:

**From `/docs/handoff/`:**
- `Central_Workspace_v3_Active_Overview.md`
- *(Optional)* any relevant `handoff_<prev>_to_<next>.md`

**From `/docs/`:**
- `portfolio_project_guidance.md`
- `project_gameplan.md`
- `manual_project_creation_checklist.md`
- *(Optional)* `next_generation_enablers.md`

**Kick-off Prompt Template:**
> Resume from the attached portfolio handoff kit.  
> We’re launching **<Project Name>** as part of Phase <#> in the Project Game Plan.  
> Follow the standards in *Portfolio Project Guidance*, initialize structure with *manual_project_creation_checklist.md*,  
> and reference *Central_Workspace_v3_Active_Overview.md* for portfolio context and open governance questions.  
> Maintain clean reasoning and attach code or data as downloadable files.

---

## 🧠 Update Rhythm

| Action | Trigger | Update |
|--------|----------|--------|
| New project start | Phase transition | Create new `Central_Workspace_v#` |
| Project completion | Lessons ready | Add to `lessons_learned_log.md`, update dashboard |
| Standards change | Any process improvement | Update `guidance.md` & `gameplan.md` |
| Governance updates | Policy or schema change | Update governance section here |

---

## 🔁 Resume Prompt
> **Resume from Central Workspace v3 Active Overview.**  
> Continue maintaining portfolio-level organization, governance, and standards.  
> SCM‑01 is currently active; ensure its results flow into future handoffs and governance updates.

---

*End of Central Workspace v3 Overview*
