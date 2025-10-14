# Network Optimization with Monte Carlo Simulation

📂 **Project Code:** LOG-03  
📄 **Context:** Logistics / Supply Chain Design  
📅 **Date:** YYYY-MM-DD

## 📌 Overview
Model supply chain network design under uncertainty using Monte Carlo simulation, compared against deterministic linear optimization.

## 🎯 Objectives
- Incorporate demand and cost uncertainty into network design.
- Evaluate probability distributions of outcomes vs single-point estimates.

## 🛠️ Methods & Tools
- **Primary:** Monte Carlo Simulation
- **Comparisons:** Scenario Analysis, Deterministic LP
- **Stack:** Python (numpy, pandas, matplotlib, pulp)
- **Data Emphasis:** *Data Analysis & Simulation* (see [Monte Carlo](../../glossary.md#-data-analysis--statistics))

## 🔍 Comparison & Justification
- *Monte Carlo:* flexible, probabilistic results.  
- *Scenario Analysis:* limited to fixed “what-if”s.  
- *LP:* efficient but deterministic.  
- **Chosen:** Monte Carlo for uncertainty quantification.

## 📊 Results
Distribution of total costs, bottleneck probabilities, heatmaps of capacity usage.

## 📈 Business Impact
Risk-aware planning, better allocation of distribution centers under uncertainty.

## 📚 References
Logistics simulation literature; BUSN501 Week 7 Flaws (fallacy avoidance).
