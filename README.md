# 📊 Analytics & Decision Intelligence Portfolio

Welcome to my professional portfolio — a curated collection of projects demonstrating how **data, models, and human reasoning** combine to solve complex business, finance, and logistics challenges.

Each project blends **technical precision** with **strategic decision design**, illustrating the evolution from classic analytics to modern **Decision Intelligence**.

---

## 🧭 Portfolio Purpose

This portfolio bridges the gap between **descriptive analytics** and **decision-centric systems** that are explainable, ethical, and adaptive.

It serves two complementary goals:

1. **Professional Showcase:** Apply advanced analytical and AI-driven methods to real-world business, finance, logistics, and HR problems.  
2. **Learning Framework:** Deepen intuitive understanding of models, parameters, and system behavior — developing mathematical, statistical, and domain fluency.

> _Every project is both a demonstration and an experiment — solving real problems while expanding mastery and reasoning._

---

## ⚙️ Portfolio Architecture

The portfolio is organized into **Core Domains** (problem contexts) and **Next-Generation Enablers** (analytical capabilities).

### 🧱 **Core Domains — Where Problems Live**

| Folder | Focus | Description |
|---------|--------|-------------|
| **Core/Data_Analytics/** | Foundational analytics | Forecasting, regression, dashboards, and optimization models that form the base of decision intelligence. |
| **Core/Supply_Chain_Logistics/** | Operations & logistics | Inventory, transportation, routing, and digital twin modeling for operational efficiency. |
| **Core/Finance/** | Financial analytics | Forecasting, valuation, ROI analysis, and capital decision models for financial planning and risk. |
| **Core/HR_People_Analytics/** | Workforce analytics | Retention, performance, and human-centered decision modeling. |

---

### 🧩 **Next-Generation Enablers — How Problems Are Solved**

Organized into three functional layers reflecting how modern decision systems evolve from intelligence to governance.

#### 🧠 **Intelligence Layer**
Focus: reasoning, modeling, and interpretability.  
- `AI_Assisted_Analytics/` — AI tools (GPT, AutoML, Copilot) accelerating analytical work.  
- `Explainable_AI/` — Transparency via SHAP, LIME, and interpretable models.  
- `Optimization_RL/` — Reinforcement learning and prescriptive optimization.  
- `Causal_Graphs/` — Modeling cause-effect relationships with Directed Acyclic Graphs (DAGs).

#### 🏗️ **System Layer**
Focus: simulation, connectivity, and systemic reasoning.  
- `Simulation_Digital_Twins/` — Virtual models of logistics and business systems for testing scenarios.  
- `Edge_IoT/` — Real-time analytics from sensors and streaming data.  
- `Knowledge_Graphs/` — Contextual data linking for semantic reasoning.  
- `Sim_Opt_Hybrids/` — Hybrid simulation-optimization models for planning and scheduling.

#### ⚖️ **Governance Layer**
Focus: ethics, transparency, and human alignment.  
- `Blockchain/` — Provenance tracking, smart contracts, and distributed trust.  
- `Responsible_AI/` — Model lineage, bias metrics, and governance dashboards.  
- `Human_AI_Collaboration/` — Decision copilots and human-AI workflow design.  
- `Generative_Support/` — LLM-driven scenario reports and automated documentation.  
- `Ethical_AI_Policy/` — Frameworks and principles for responsible AI practice.

---

## 🧠 Learning & Mastery Framework

Every project reflects **two complementary dimensions**:

| Dimension | Focus |
|------------|--------|
| **External Goal – Professional Showcase** | Apply analytical methods or technologies to realistic, data-driven business problems. |
| **Internal Goal – Learning & Mastery** | Develop mathematical/statistical fluency, understand parameter sensitivity, and expand professional vocabulary. |

Each project README addresses:
- Problem & scenario  
- Methods and enablers applied  
- Solution & insight  
- Reflection on learning and terminology  

---

### 📈 Project Progression (Updated)

| Tier | Project | Theme / Focus |
|------|----------|---------------|
| **1. Decision Intelligence Foundation** | `LOG-02_forecasting_inventory_policies` | Forecasting → Inventory Policy → Simulation (first end-to-end Decision Intelligence case) |
| **2. Core Analytics Refresh** | `DA-01_churn_prediction_logit` | Classical modeling, interpretation, and explainability |
|  | `DA-03_time_series_forecasting` | Forecasting fundamentals; statistical vs. ML comparison |
| **3. Advanced Logistics Modeling** | `LOG-03_network_optimization_montecarlo` | Optimization, stochastic modeling, uncertainty |
| **4. AI-Assisted Layer** | `AI-02_ai_forecasting_retail_demand` | Compare classical and AI forecasting models |
|  | `AI-04_generativeai_supplychaindocs` | Automated narrative generation for supply-chain decisions |
| **5. Governance & Trust Layer** | `BLK-03_pharma_serialization_dscsa_sim` | Blockchain traceability and compliance simulation |
| **6. New Enabler Builds** | `SIM-01_policy_robustness_simulator` | Simulation / Digital Twin |
|  | `KG-01_logistics_graph_inference` | Knowledge Graph reasoning |
|  | `GOV-01_model_audit_bias_check` | Responsible AI auditing |

---

## 📚 Supporting Documents

| File | Purpose |
|------|----------|
| [`docs/Next_Generation_Enablers.md`](docs/Next_Generation_Enablers.md) | Detailed definitions of each enabler and its learning focus. |
| [`docs/PROJECT_GAMEPLAN.md`](docs/PROJECT_GAMEPLAN.md) | The roadmap outlining progression, goals, and applied outcomes. |
| [`docs/glossary.md`](docs/glossary.md) | Central reference for technical and industry vocabulary. |
| [`assets/next_decade_analyst_framework.png`](assets/next_decade_analyst_framework.png) | Visual summary of the Next-Decade Analyst Framework. |

---

## 🧰 Developer Tools

These tools maintain and verify the structure of this portfolio across systems.

| Tool | Location | Description |
|------|-----------|--------------|
| **verify_structure.ps1** | `_tools/verify_structure.ps1` | PowerShell script that validates the portfolio directory tree on Windows. |
| **verify_structure.sh** | `_tools/verify_structure.sh` | Linux/macOS/WSL version of the structure verifier for Bash environments. |
| **Portfolio.code-workspace** | root | VS Code workspace configuration linking all folders and docs. |
| **environment.yml** | root | Reproducible Conda environment for Python dependencies. |
| **PORTFOLIO_INIT.log** | `docs/` | Chronological record of all structural changes. |

> 💡 These utilities ensure consistency and reproducibility across Windows, WSL, and Linux environments.  
> Future additions (e.g., setup scripts, sync automation) will live in the `_tools/` folder.

---

## ⚙️ Environment Quick Start

This portfolio is designed to be fully reproducible on **Windows**, **WSL**, or **Linux** systems using VS Code.

### 🧰 Recommended Local Setup

| Tool | Purpose | Notes / Download |
|------|----------|------------------|
| **VS Code** | Main IDE for coding, Jupyter notebooks, and documentation. | [code.visualstudio.com](https://code.visualstudio.com/) |
| **Anaconda (Python 3.10+)** | Manages Python environments, dependencies, and Jupyter integration. | [anaconda.com/download](https://www.anaconda.com/download) |
| **Git** | Version control and GitHub synchronization. | [git-scm.com/downloads](https://git-scm.com/downloads) |
| **PowerShell 7+** | Modern Windows shell for running `.ps1` scripts. | Pre-installed on Windows 10/11; upgrade via [Microsoft Store](https://aka.ms/powershell). |
| **Windows Subsystem for Linux (WSL 2)** | Optional: provides a native Linux environment inside Windows. | [WSL installation guide](https://learn.microsoft.com/windows/wsl/install) |

### 🧩 Folder Conventions

| Folder | Purpose |
|---------|----------|
| **Core/** | Contains applied analytics projects organized by domain. |
| **Enablers/** | Holds next-generation analytical technologies (AI, simulation, blockchain, etc.). |
| **docs/** | Portfolio documentation, project plans, and glossary. |
| **assets/** | Visuals, framework diagrams, and exported charts. |
| **_tools/** | Maintenance scripts and utilities (cross-platform). |

### 🧠 Environment Activation

Once Anaconda is installed:

```bash
# Create the environment from file
conda env create -f environment.yml

# Activate the portfolio environment
conda activate analytics_portfolio
```

---

## 🧩 Guiding Principle

> **“Understanding replaces automation.”**  
> Every model, graph, and system here is intentionally designed — not copied or opaque — connecting **data, reasoning, and decisions** in a transparent way.

---

**Author:** James Beall  
**Focus Areas:** Business Analytics • Supply Chain • Finance • Decision Intelligence  
**Location:** Southern California  
**Contact:** [LinkedIn](#) (add link)
