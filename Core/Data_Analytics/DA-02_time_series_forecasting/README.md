# Time Series Forecasting (ARIMA vs ETS vs Prophet)

📂 **Project Code:** DA-03  
📄 **Context:** Data Analytics / MSABA  
📅 **Date:** YYYY-MM-DD

## 📌 Overview
Forecast demand using historical sales; compare ARIMA, ETS, and Prophet across total → store → category hierarchy.

## 🎯 Objectives
- Build accurate forecasts; quantify error (RMSE, MAPE).
- Explain model choice in business terms.

## 🛠️ Methods & Tools
- **Primary:** ARIMA (statsmodels)
- **Comparisons:** ETS (Exponential Smoothing), Prophet
- **Stack:** Python (pandas, statsmodels, prophet), matplotlib
- **Data Emphasis:** *Data Analysis, AI/ML* (see [ARIMA](../../glossary.md#-data-analysis--statistics))

## 🔍 Comparison & Justification
- **ARIMA vs ETS vs Prophet**  
  - *ARIMA:* handles autocorrelation/trend via differencing; best for stationary series.  
  - *ETS:* strong for level/trend/seasonality without AR terms.  
  - *Prophet:* robust to holidays/business calendars, quick modeling.  
- **Chosen:** **ARIMA** if it minimizes MAPE without overfit; switch to **ETS** for dominant seasonality or **Prophet** when holiday effects matter.

## 📊 Results
Backtest accuracy by hierarchy level; forecast plots with intervals.

## 📈 Business Impact
Lower stockouts/overstock; improved service levels and working capital.

## 📚 References
Forecasting texts; BUSN501 Week 5 discussion (ARIMA explainer).
