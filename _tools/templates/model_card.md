# Model Card — <Project Name>

## 1. Overview
- **Use case:** <what decision this supports>
- **Stakeholders:** <operators, reviewers, decision-makers>
- **Data timeframe & granularity:** <e.g., weekly demand, 2019–2024>

## 2. Data
- **Sources:** <files/tables/APIs>
- **Target:** <what you predict or optimize>
- **Key features:** <feature list + rationale>
- **Data quality checks:** <nulls, outliers, leakage guards>

## 3. Method
- **Approach:** <ARIMA/ETS/ML; inventory policy; simulation>
- **Parameters:** <key params + why>
- **Assumptions:** <stationarity, service level, lead time>

## 4. Evaluation
- **Metrics:** <MAPE, service level, stockouts, holding>
- **Backtest setup:** <windows, horizon>
- **Sensitivity/what-if:** <which knobs and ranges>

## 5. Governance
- **Versioning:** <git commit, config hash>
- **Risks/limits:** <data drift, seasonality shifts>
- **Operationalization:** <how to re-train / re-run / re-baseline>

## 6. Results Snapshot
- **Key KPIs:** <baseline vs candidate>
- **Decision implications:** <how to use the dashboard>
