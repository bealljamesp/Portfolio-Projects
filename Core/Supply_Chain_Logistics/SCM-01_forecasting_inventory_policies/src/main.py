from __future__ import annotations
from pathlib import Path
import numpy as np

from src.bootstrap import init_project
from src.forecasting import ensure_raw_exists, load_raw, naive_forecast_stats
from src.inventory import build_policy
from src.simulation import simulate_sQ


def _annualize(mu_week: float) -> float:
    return mu_week * 52.0


if __name__ == "__main__":
    env = init_project()
    RAW_DIR = env["RAW_DIR"]
    CONFIG = env["CONFIG"]
    SEED = env["SEED"]

    # 1) Data
    raw_path = ensure_raw_exists(RAW_DIR, seed=SEED)
    df = load_raw(raw_path)

    # 2) Forecast (baseline)
    fc = naive_forecast_stats(df, last_n=52)
    print(f"[Forecast] mean_weekly={fc.mean_weekly:.1f}, sd_weekly={fc.sd_weekly:.1f}")

    # 3) Policy (EOQ + Normal safety stock)
    policy = build_policy(
        mu_week=fc.mean_weekly,
        sd_week=fc.sd_weekly,
        L_days=float(CONFIG.get("lead_time_days", 14)),
        service=float(CONFIG.get("service_level_target", 0.95)),
        D_annual=_annualize(fc.mean_weekly),
        K=float(CONFIG.get("order_cost", 150.0)),
        h_rate=float(CONFIG.get("holding_cost_rate", 0.25)),
        unit_cost=float(CONFIG.get("unit_cost", 10.0)),
    )
    print(
        f"[Policy] Q={policy.Q:.1f}, s={policy.s:.1f}, z={policy.z:.2f}, SS={policy.ss:.1f}"
    )

    # 4) Simulation (12 months of demand from historical distribution)
    rng = np.random.default_rng(SEED)
    demand_weeks = 52
    # draw iid weekly from historical mean/sd (baseline toy)
    sim_dem = (
        rng.normal(loc=fc.mean_weekly, scale=max(1e-6, fc.sd_weekly), size=demand_weeks)
        .clip(min=0)
        .round()
    )
    res = simulate_sQ(
        demand=sim_dem,
        policy_s=policy.s,
        policy_Q=policy.Q,
        lead_time_days=float(CONFIG.get("lead_time_days", 14)),
        review_period_days=float(CONFIG.get("review_period_days", 7)),
        initial_inventory=None,
        seed=SEED,
    )
    print(
        f"[Sim] service={res.service_level:.3f}, avg_inv={res.avg_inventory:.1f}, stockouts={res.stockouts}, orders={res.orders_placed}"
    )
