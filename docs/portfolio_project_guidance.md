# 🎯 Portfolio Project Guidance — Tone, Intent & Operating Principles

**Audience:** Future project chats and initialization prompts (DA-01, SCM-02, AI-01, etc.), hiring managers, and subject-matter experts (SMEs).
**Primary intent:** Build a **professional, recruiter-ready portfolio** that demonstrates analytical rigor, decision relevance, and industry fluency.
**Equally important intent:** Create a **living laboratory for learning** — every project deepens real understanding of forecasting, optimization, simulation, and explainable analytics.

> 🧭 Guiding Motto: **Predictable, Not Mysterious**
> Every system, model, and result should behave in ways that are **transparent, explainable, and reproducible**.
> No “magic,” no guessing — only well-reasoned, traceable outcomes.

---

## 1️⃣ Identity & Focus — Decision Intelligence Professional
The portfolio reflects the mindset of a **Decision Intelligence (DI) Professional** — someone who **connects data, models, and managerial judgment** to improve real-world decisions.

**Next-Decade Skills (anchor):**
- **AI-assisted analytics** – copilots for reasoning, explanation, and efficiency
- **Simulation & optimization** – “what-if” experimentation and trade-off analysis
- **Causal & explainable methods** – intuitive, defensible reasoning over black boxes
- **Business intelligence fluency** – storytelling, KPIs, cost-benefit framing
- **Governance & ethics awareness** – traceability, versioning, responsible AI

---

## 2️⃣ Operating Principles (applied in every project)

1. **Reproducibility Contracts**
   - Strict version pins (`pyproject.toml`).
   - First-cell **Sanity Check** prints Python/lib versions, config hash, git commit, and random seed.
   - One **Source of Truth** for data under `/data/`.

2. **Explainability First**
   - Prefer simple, transparent baselines before sophistication.
   - Document assumptions, parameters, and failure modes **as you go**.
   - Every metric and visualization must be *defensible*.

3. **Business Impact Orientation**
   - Analyses tie directly to *decisions and actions*: what changes, why, and at what cost or risk.
   - KPIs and trade-offs are explicit and manager-friendly.

4. **Build Intuition, Avoid Mystery**
   - Every model should make intuitive sense; if not, simplify until it does.
   - Include small derivations, sanity plots, and comments linking math ↔ business meaning.
   - “If we can’t defend it, we don’t ship it.”

5. **Industry Standards Over Academic Demos**
   - Use realistic scenarios, naming conventions, and KPIs used by practitioners.
   - Reference benchmarks (service level, fill rate, ROI) common in the industry domain.
   - Projects must look and feel like professional case studies, not classroom exercises.

6. **Simulation as Learning Tool**
   - Treat every project as a controllable sandbox for experimentation.
   - Generate or regenerate data to illustrate mastery of forecasting, optimization, and policy reasoning.
   - Emphasize reproducible experiments and structured sensitivity analysis.

7. **Governance Awareness**
   - Traceability from code → config → result.
   - Integrate integrity checks (`check_portfolio_integrity.py`) and pytest validations.
   - Capture decisions in `notes.md` and `lessons_learned_log.md`.

---

## 3️⃣ Communication Norms (for Chats & Notebooks)

- **Keep chats clean.** Long code or data → attach as files, not giant chat blocks.
- Use **summary bullets and checklists** for reasoning steps.
- Surface **alternatives and trade-offs** proactively (“Option A vs B — recommend A because…”).
- Maintain consistent, professional tone.
- When exploring theory, link to portfolio glossary and tag with project (e.g., *SCM-01*).

---

## 4️⃣ Required Artifacts (per Project)

| Artifact | Purpose |
|-----------|----------|
| `pyproject.toml` | Dependency and Ruff config (strict pins). |
| `config.yaml` | Parameters, paths, seeds, reproducibility. |
| **Notebook** | End-to-end workflow with Sanity Check cell. |
| `model_card.md` | Data, method, evaluation, governance summary. |
| `reports/decision_dashboard_spec.md` | Managerial dashboard design & KPIs. |
| `tests/` | At least one config and I/O sanity test. |
| `reports/figures/` | Decision visuals. |
| `README.md` | Purpose, run instructions, status badges. |
| `notes.md` | Running log of reasoning and open questions. |

---

## 5️⃣ Review & Defense Readiness (SME-Proof Checklist)

Before marking any project complete, verify:
- **Decision clarity** – Who uses it and how?
- **Assumptions documented** – horizon, stationarity, costs, constraints.
- **Sensitivity explored** – outputs vs. key knobs.
- **Limitations stated** – edge cases and blind spots.
- **Traceability confirmed** – commit hash + config hash + seed captured.
- **Baselines compared** – simple models shown and discussed.
- **Integrity check + pytest pass** on fresh environment.

If you can’t **defend it like a dissertation** or **justify it like an industry case**, iterate until you can.

---

## 6️⃣ Project Category Examples

| Category | Typical Question | Example Project |
|-----------|------------------|-----------------|
| **Forecast → Policy → Simulation → Decision** | “How much to order and when?” | SCM-01 Inventory Policies |
| **Classification / Retention** | “Which customers are likely to churn?” | DA-01 Churn Prediction |
| **Optimization / Pricing** | “What mix or price maximizes profit?” | LOG-03 Product-Mix Optimization |
| **Governance / Explainability** | “How do we trust model results?” | GOV-01 Explainable AI Audit |

---

## 7️⃣ Language & Tone

- **Professional, decision-centric, and confident.**
- Every explanation links back to *business impact*.
- Use **industry lingo** consistently; expand glossary as new terms arise.
- Translate statistical findings into *actionable insights*.

---

## 8️⃣ Quality Gates (“Done” Definition)

- `python _tools/check_portfolio_integrity.py` → ✅ PASS
- `python _tools/check_portfolio_integrity.py --run-pytest` → ✅ PASS
- Notebook runs top-to-bottom deterministically (seeded).
- Model card and dashboard spec updated and committed.
- Figures saved to `reports/figures/` and referenced in docs.

---

## 9️⃣ Project Kick-off Packet (Pass to New Chat)

Include:
- This guidance doc (`docs/portfolio_project_guidance.md`)
- `docs/project_gameplan.md` (roadmap)
- `docs/manual_project_creation_checklist.md` (step-by-step)
- Any snapshot relevant to the phase (`docs/snapshots/*.md`)
- Project’s **summary prompt**, e.g.:

> **Kick-off Prompt Template**
> “Continue from the Portfolio Guidance.
> We’re building **<Project Name>** to reinforce reproducibility, explainability, and decision impact.
> Follow the checklist, scaffold structure, update config/pyproject/model card, add tests, and run integrity checks.
> Keep chat clean — long code as downloadable files.”

---

## 🔟 Anti-Imposter Practices

- Validate understanding through derivations, plots, and simulations.
- Record questions and answers in `notes.md` and glossary.
- Confidence comes from **clarity**, not certainty.
- “Predictable, Not Mysterious” is the standard for both code and reasoning.

---

*File location:* `Portfolio/docs/portfolio_project_guidance.md`
*Use this at the start of every new project chat to maintain consistent tone, standards, and analytical integrity.*
