![Python](https://img.shields.io/badge/python-3.11-blue)
![License](https://img.shields.io/badge/license-MIT-green)

# Portfolio Index

This repository hosts **13 projects** across four groups. Each project folder contains data placeholders (or synthetic data in the AnswerKey), Jupyter notebooks, and a README.

> If you have not yet run the reorg script, your folders may be named like `ai-01_*` and `log-02-*`. After reorg, they'll be under `ai/`, `msaba/`, `logistics/`, and `scm_ai/` with numeric prefixes.

## MSABA (4)
1. **01_churn_prediction_logit** — Customer churn classification with logistic regression and evaluation.  
2. **02_ab_testing_experiment_design** — A/B test analysis, confidence intervals, and power.  
3. **03_time_series_forecasting** — Classical forecasting with lag-based ML baseline.  
4. **04_pricing_product_mix_optimization** — MILP: pricing/product-mix under budget & SKU constraints.

## Logistics (3)
1. **01_sql_python_excel_kpis_dashboard** — ETL from CSVs, KPI trends, revenue/margin visuals.  
2. **02_forecasting_inventory_policies** — Demand forecasting + EOQ/ROP/Safety Stock.  
3. **03_network_optimization_monte_carlo** — Facility location & shipping-cost model + risk simulation.

## AI Portfolio (4)
1. **01_customer_churn_explainableai** — SHAP/LIME explainability + fairness slice metrics.  
2. **02_ai_forecasting_retail_demand** — Prophet vs. ML (RF/LSTM) + cost-of-error simulation.  
3. **03_computer_vision_logistics** — CNN for defect detection in warehouse QC.  
4. **04_generativeai_supplychaindocs** — LLM-based contract summaries and risk tagging.

## SCM + AI Crossover (2)
1. **01_ai_inventory_optimization** — ML demand → EOQ/ROP/SS + Monte Carlo service-levels.  
2. **02_digital_twin_supplychain** — SimPy digital twin + ML bottleneck predictor.

---

## Quickstart

```bash
conda env create -f environment.yml
conda activate ai-scm-portfolio
jupyter lab
```

- Open any project’s `notebooks/` folder and **Run All** (AnswerKey versions).  
- For learning builds, use the non-AnswerKey versions and add data as instructed per README.

---

## Folder Map (after reorg)

```
.
├── ai/
│   ├── 01_customer_churn_explainableai/
│   ├── 02_ai_forecasting_retail_demand/
│   ├── 03_computer_vision_logistics/
│   └── 04_generativeai_supplychaindocs/
├── msaba/
│   ├── 01_churn_prediction_logit/
│   ├── 02_ab_testing_experiment_design/
│   ├── 03_time_series_forecasting/
│   └── 04_pricing_product_mix_optimization/
├── logistics/
│   ├── 01_sql_python_excel_kpis_dashboard/
│   ├── 02_forecasting_inventory_policies/
│   └── 03_network_optimization_monte_carlo/
├── scm_ai/
│   ├── 01_ai_inventory_optimization/
│   └── 02_digital_twin_supplychain/
└── portfolio-hub/  _Archive/  _Reference/
```

---

### Notes
- Keep **AnswerKey** copies in `Portfolio_AnswerKey/` to compare outputs while you build the primary versions.
- Consider adding GitHub Actions to smoke-test notebooks (optional; can be slow).
