# Pricing & Product Mix Optimization (LP vs MILP)

📂 **Project Code:** DA-04  
📄 **Context:** Data Analytics / MSABA  
📅 **Date:** YYYY-MM-DD

## 📌 Overview
Optimize product mix and pricing to maximize profit under budget, capacity, and SKU constraints.

## 🎯 Objectives
- Formulate objective & constraints; deliver optimal plan.
- Sensitivity analysis on prices and constraints.

## 🛠️ Methods & Tools
- **Primary:** MILP (Mixed Integer Linear Programming)
- **Comparisons:** LP (continuous), Heuristics
- **Stack:** Python (pulp/ortools), pandas
- **Data Emphasis:** *Optimization & Data Analysis* (see [glossary](../../glossary.md#-data-analysis--statistics))

## 🔍 Comparison & Justification
- **MILP vs LP vs Heuristics**  
  - *MILP:* handles discrete SKUs, on/off decisions.  
  - *LP:* faster but can’t model integrality.  
  - *Heuristics:* quick but no optimality guarantees.  
- **Chosen:** **MILP** for discrete decisions; fall back to **LP** for continuous blends.

## 📊 Results
Optimal SKU plan; binding constraints; shadow prices; scenario comparisons.

## 📈 Business Impact
Higher profit and better resource allocation; transparent trade-offs.

## 📚 References
Optimization references; BUSN501 discussions on evidence/reasoning.
