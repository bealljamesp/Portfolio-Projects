![Status](https://img.shields.io/badge/status-active-brightgreen)
![Reproducible](https://img.shields.io/badge/reproducible-seeded-blue)
![Notebook](https://img.shields.io/badge/entry-notebook-black)

# 🏗️ SCM-01 — Forecasting → Inventory → Simulation → Decision

📂 **Domain:** Supply-Chain & Logistics
📄 **Project Code:** SCM-01_forecasting_inventory_policies
📅 **Status:** Active — Phase 1 “Decision Foundations”

---

## 📘 Overview
This project initiates the portfolio’s decision-intelligence pipeline.
It connects **demand forecasting**, **inventory policy modeling**, and **simulation-based decision analysis** into a unified workflow.

**Goal:** design an explainable system that forecasts demand, converts those forecasts into stocking policies, and evaluates their performance through simulation and cost metrics.

---

## 🎯 Objectives
1. Forecast demand using time-series or regression models.
2. Translate forecasts into inventory policies (EOQ, (Q,R), or service-level).
3. Simulate uncertain demand and lead times to test policy performance.
4. Evaluate trade-offs between service level, cost, and stability.
5. Produce transparent, reproducible results suitable for governance review.

---

## 🧰 Methods & Tools
| Category | Tools / Techniques |
|-----------|--------------------|
| **Data Handling** | pandas • numpy • scipy • openpyxl |
| **Modeling** | ARIMA / ETS / Prophet • EOQ • (Q,R) policy |
| **Simulation** | Monte Carlo • SimPy • NumPy randomization |
| **Visualization** | matplotlib • plotly • seaborn |
| **Governance Docs** | model_card.md • README reflection • parameter log YAML |

---

## 🔍 Methodology Flow
```text
Forecasting  →  Policy Modeling  →  Simulation  →  Decision Metrics
      |               |                   |
  Historical data   Service levels     KPI visualization
