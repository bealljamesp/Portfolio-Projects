# 🧭 Central Handoff Standards (v1.0)

**Purpose:**  
Define the standard structure and expectations for project handoffs to Central Workspace.  
Ensure continuity, reproducibility, and portfolio-wide learning across GPT instances.

---

## 1️⃣ Handoff Purpose
Each project concludes with a structured transfer of all relevant files, insights, and standards updates to Central Workspace.  
Central acts as the *portfolio integrator*, responsible for maintaining documentation, updating templates, and preparing the next project.

---

## 2️⃣ Required Handoff Package Contents

| Artifact | Description | Source |
|-----------|--------------|--------|
| **Project Overview** | Narrative summary of scenario, objectives, and analytical plan. | `*_Project_Overview.md` |
| **Lessons Log (Project-Level)** | Detailed log of "wish I had known" moments. | `*_lessons_log.md` |
| **Carryover Summary** | Condensed Markdown summary for next GPT instance. | `*_carryover.md` |
| **Core Artifacts** | README, model card, config, and reproducibility scripts. | Project root |
| **Governance Updates** | Standards, process changes, or template updates identified during project. | `*_handoff_todo.md` |
| **Archive Bundle** | Compressed folder with all final project materials. | Exported zip |

---

## 3️⃣ Central Responsibilities

1. **Receive Handoff:** Import project deliverables and documentation.  
2. **Integrate Lessons:** Summarize or append project-level lessons into `docs/lessons_learned_log.md`.  
3. **Refresh Templates:** Update `manual_project_creation_checklist.md` and `portfolio_project_guidance.md` with new standards.  
4. **Update Dashboard:** Add project metadata (phase, status, last updated) to `central_dashboard.md`.  
5. **Prepare Next Project:** Use the latest guidance and templates to initialize the next project workspace.

---

## 4️⃣ Portfolio-Wide Standards Central Tracks

| Category | Description |
|-----------|--------------|
| **File Naming** | `{CODE}_{descriptor}.md` (e.g., `SCM-01_Project_Overview.md`) |
| **Lifecycle Model** | Kick-off → Development → Governance Review → Handoff |
| **Documentation Policy** | Long outputs as downloadable files to minimize DOM load |
| **Reproducibility** | Config-driven, seeded, and pinned environments |
| **Lessons System** | Project-level logs summarized to portfolio-level log |
| **Continuous Improvement** | Governance updates captured in `*_handoff_todo.md` |

---

## 5️⃣ Standards Improvement Queue (To Implement Portfolio-Wide)

| Improvement | Description | Status |
|--------------|--------------|---------|
| **Governance Stage Summary cell** | Auto-record config hash, seed, and environment metadata in each notebook. | Pending |
| **project_manifest.json** | Machine-readable record of paths, versions, and key outputs. | Pending |
| **central_dashboard.md** | Live index of projects with metadata (phase, last update, outputs). | Pending |
| **README Reflections section** | Add a short reflection or key takeaway summary to README templates. | Pending |
| **Experimental Sandbox tag** | Mark non-reproducible exploratory code clearly. | Pending |

---

**Version:** 1.0  
**Last Updated:** 2025-10-14  
**Maintainer:** Central Workspace Governance Layer

---
