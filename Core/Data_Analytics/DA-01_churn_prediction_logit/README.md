# Customer Churn Prediction (Logistic Regression vs Tree Ensembles)

📂 **Project Code:** DA-01  
📄 **Context:** Data Analytics / MSABA  
📅 **Date:** YYYY-MM-DD

## 📌 Overview
Predict customer churn and quantify retention ROI using historical customer, interaction, and label data.

## 🎯 Objectives
- Build a baseline, interpretable model to predict churn.
- Identify top drivers of churn; estimate lift from targeted retention offers.

## 🛠️ Methods & Tools
- **Primary:** Logistic Regression
- **Comparisons:** Random Forest, XGBoost
- **Stack:** Python (pandas, scikit-learn), matplotlib
- **Data Emphasis:** *Data Analysis, AI/ML* (see [glossary](../../glossary.md#-data-analysis--statistics))

## 🔍 Comparison & Justification
- **LogReg vs Random Forest/XGBoost**  
  - *LogReg:* interpretable coefficients, quick baseline, good with linear/monotonic signals.  
  - *RF/XGB:* higher accuracy on non-linear interactions; less transparent without SHAP.  
- **Chosen:** Start with **LogReg** for stakeholder clarity; benchmark against **RF/XGB**. If lift ≥ X% with acceptable explainability, graduate to tree ensembles.

## 📊 Results
- AUC/PR, calibration plot; top features (odds ratios); expected retention ROI by decile.

## 📈 Business Impact
Prioritize outreach to top-risk deciles to reduce churn and improve LTV.

## 📚 References
BUSN501 discussions on evidence/reasoning; industry churn literature.
