# SCM-01 Project Overview — Forecasting & Inventory Policies

📂 **Project Code:** SCM-01_forecasting_inventory_policies  
📅 **Phase:** Decision Foundations  
📘 **Portfolio Context:** Phase 1 baseline for Forecast → Inventory → Simulation → Decision workflows  

---

## 🧭 Scenario
You are serving as a decision intelligence analyst for a retail company managing multiple stores and product categories.  
The company wants to transition from reactive inventory management to a **data-driven, explainable forecasting and policy system**.

The organization’s leadership expects a clear, defendable analytical process that links **demand forecasting**, **inventory policy setting**, **simulation-based evaluation**, and **business-ready decision recommendations.**

---

## 🎯 Objective
Design a **predictable, reproducible workflow** that connects forecasting, policy modeling, and simulation into an interpretable decision framework.

**Business Question:**  
> “Given our demand patterns, service targets, and cost structure, what inventory policy achieves the best balance between service level and total cost?”

---

## 🧩 Analytical Plan
| Phase | Focus | Deliverable | Key Question |
|-------|--------|--------------|---------------|
| **1. Forecasting** | Estimate expected demand using time-series baselines (e.g., seasonal-naïve, moving average). | Forecast plots, metrics | “What is our expected demand per SKU per period?” |
| **2. Inventory Policy** | Convert forecast + uncertainty into an order-up-to policy. | Policy table, safety stock levels | “How much should we stock to achieve our service target?” |
| **3. Simulation** | Test inventory behavior over time under review period and lead time. | KPIs, cost-service tradeoffs | “How does the policy perform under realistic operations?” |
| **4. Decision Layer** | Aggregate insights and present explainable recommendations. | Dashboard, model card, decision summary | “Which policy delivers the desired service at acceptable cost?” |

---

## ⚙️ Modeling Approach
- **Forecasting:** Seasonal-naïve and moving-average baselines (extendable to ARIMA/Prophet).
- **Policy:** Periodic-review (P) with order-up-to level derived from mean + safety stock (via z-factor).  
- **Simulation:** Day-level deterministic lead-time flow, computing on-hand, backlog, service, and cost KPIs.  
- **Decision:** Multi-scenario runs (90/95/98% service levels) summarized into a cost–service frontier.

---

## 🧠 Governance & Learning Focus
This project anchors the portfolio’s *Decision Foundations* phase.  
It emphasizes **transparency, explainability, and reproducibility** through:
- Central configuration in `config.yaml`
- Controlled random seeds for deterministic output
- Version-pinned dependencies
- Documented assumptions and reasoning trail (via `notes.md` and model card)

Each analytical choice should be **traceable, defendable, and repeatable**, aligning with the “Predictable, Not Mysterious” principle.

---

## 📊 Expected Outputs
- Forecast accuracy summary (MAE, sMAPE)  
- Inventory simulation results: service %, fill rate, cost breakdown  
- Cost–service tradeoff chart  
- Model card documenting purpose, assumptions, limitations  
- Dashboard specification for management reporting  

---

## 🔄 Next Steps
1. Review existing SCM-01 assets for alignment with this baseline.
2. Verify forecasting → policy → simulation linkage is intact and modular.
3. Update `notes.md` with parameter decisions and rationale.
4. Prepare Phase 1 summary visuals and management brief.

---

**Author:** Portfolio Decision Intelligence Track  
**Last Updated:** 2025-10-14
