# A/B Testing & Experiment Design (Conversion & Revenue Lift)

📂 **Project Code:** DA-02  
📄 **Context:** Data Analytics / MSABA  
📅 **Date:** YYYY-MM-DD

## 📌 Overview
Design and analyze controlled experiments to estimate conversion/revenue lift while accounting for novelty and seasonality.

## 🎯 Objectives
- Compute effect sizes, CIs, and p-values.
- Power analysis & sample size planning.

## 🛠️ Methods & Tools
- **Primary:** Two-proportion tests, t-tests, bootstrap CIs
- **Comparisons:** Bayesian A/B, CUPED variance reduction
- **Stack:** Python (pandas, scipy, statsmodels), Excel
- **Data Emphasis:** *Data Analysis, Statistics* (see [glossary](../../glossary.md#-data-analysis--statistics))

## 🔍 Comparison & Justification
- **Classical vs Bayesian vs CUPED**  
  - *Classical:* familiar, fast, clear CIs/p-values.  
  - *Bayesian:* intuitive probability statements; flexible priors.  
  - *CUPED:* reduces variance using pre-experiment covariates.  
- **Chosen:** Start **Classical** with CUPED when pre-period data available; consider **Bayesian** when continuous monitoring or small samples.

## 📊 Results
Effect estimates with 95% CIs; power curves; sensitivity to novelty/seasonality.

## 📈 Business Impact
More reliable go/no-go decisions on product or marketing changes.

## 📚 References
Experiment design best practices; BUSN501 reasoning/fallacy avoidance.
