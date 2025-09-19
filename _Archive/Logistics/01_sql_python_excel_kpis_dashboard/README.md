# SQL + Python KPIs + Excel Dashboard

Join retail/warehouse datasets with SQL, compute KPIs in pandas, and build an Excel pivot dashboard.

## 1) Business Problem
- Context and the single guiding question.
- Why it matters (revenue, cost, efficiency).

## 2) Data & Preparation
- Sources, rows/columns, key features.
- Cleaning/feature engineering summary.
- Data dictionary link (if any).

## 3) Methods & Tools
- Techniques used (e.g., logistic regression, ARIMA, MILP).
- Why chosen (interpretability, constraints, robustness).
- Stack: Python (pandas, scikit-learn, etc.).

## 4) Results
- Core metrics/outputs in a simple table.
- 1–2 visuals (ROC, forecast vs actual, network map).

## 5) Business Insights & Impact
- Bullet-point recommendations.
- Estimated impact (assumptions stated).
- Risks/limitations.

## 6) Reflection / Next Steps
- What you learned.
- How you’d extend with more data/time.

## 7) How to Reproduce
```bash
# create and activate a virtual environment (Windows PowerShell)
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# install dependencies
pip install -r requirements.txt

# launch Jupyter
jupyter lab  # or: jupyter notebook
```
- Place data files under `data/raw/` (or use the provided `sample/` subset).
- Open notebooks in `notebooks/` and run top-to-bottom.

## Repository Layout
```
project-template/
├─ notebooks/           # EDA, modeling, experiments
├─ src/project_name/    # Reusable functions, pipelines
├─ data/
│  ├─ raw/              # .gitignored
│  └─ processed/        # .gitignored
├─ reports/figures/     # .gitignored plots/exports
├─ docs/                # case study, slides
├─ tests/               # (optional) unit tests
├─ requirements.txt
└─ .gitignore
```

## License
MIT
