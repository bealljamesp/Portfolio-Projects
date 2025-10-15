# 📘 Portfolio Lessons Learned Log

**Purpose:**
Document insights, outcomes, and transferable lessons from each project to strengthen the portfolio’s collective intelligence and reproducibility standards.

Each entry should summarize what was learned technically, organizationally, and conceptually.
Use this log as both a historical record and a feedback mechanism for improving the manual project creation checklist and governance framework.

---

## 🧭 Format Overview

| Section | Description |
|----------|-------------|
| **Summary** | A short paragraph describing what the project accomplished and how it fits into the portfolio. |
| **Technical Wins** | Successful implementations, efficient methods, or breakthroughs that worked well. |
| **Pain Points** | Frictions, issues, or areas that caused inefficiency or confusion. |
| **Process Lessons** | Workflow or organizational improvements learned during development. |
| **Governance Insights** | Key takeaways on traceability, ethics, reproducibility, or model explainability. |
| **Next Project Prep** | Adjustments or recommendations for the next project phase. |

---

## 🧩 Example Entry – SCM-01 Forecasting Inventory Policies

**Summary:**
Developed a forecasting-to-decision pipeline integrating demand prediction, inventory policy simulation, and dashboard planning. Established baseline reproducibility contracts and structural standards for all future projects.

**Technical Wins:**
- Sanity Check Cell successfully standardized environment validation.
- Integrity Checker confirmed project reproducibility across environments.
- Established config-driven forecasting and simulation parameters.

**Pain Points:**
- Duplicated data folders caused early confusion before standardizing SoT (`data/`).
- Initial notebook lacked deterministic seeding until added later.

**Process Lessons:**
- Run integrity check before modeling to catch config and directory issues early.
- Keep `model_card.md` and `decision_dashboard_spec.md` under development alongside the code—not afterward.

**Governance Insights:**
- Sanity Check Cell metadata (config hash, git commit) proved valuable for traceability.
- Explicit model cards improved communication of analytical decisions.

**Next Project Prep:**
- Use `pyproject_portfolio.toml` template from `_tools/templates` for consistent dependency pins.
- Begin DA-01 with the same structure, emphasizing interpretable model explainability.

---

## 📜 New Entry Template

### Lessons Learned – [Project Name]

**Summary:**
> *(Describe project focus and results in 3–4 sentences.)*

**Technical Wins:**
-

**Pain Points:**
-

**Process Lessons:**
-

**Governance Insights:**
-

**Next Project Prep:**
-

---

*End of Log*
