from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import numpy as np
import pandas as pd


@dataclass
class ForecastResult:
    mean_weekly: float
    sd_weekly: float
    horizon_weeks: int = 1


def generate_synthetic_weekly(
    n_weeks: int,
    level=200,
    trend=0.0,
    season_amp=0.0,
    promo_uplift=0.0,
    promo_freq=0.0,
    noise_sd=20,
    seed=42,
) -> pd.DataFrame:
    """Simple synthetic weekly demand generator (Sunday-end weeks)."""
    rng = np.random.default_rng(seed)
    t = np.arange(n_weeks)
    seasonal = season_amp * np.sin(2 * np.pi * t / 52)
    promos = (rng.random(n_weeks) < promo_freq).astype(int)
    demand = level + trend * t + seasonal + promos * promo_uplift * (level + seasonal)
    demand = np.maximum(0, rng.normal(demand, noise_sd))
    df = pd.DataFrame(
        {
            "date": pd.date_range("2020-01-05", periods=n_weeks, freq="W-SUN"),
            "demand_qty": demand.round().astype(int),
            "promo_flag": promos,
        }
    )
    return df


def naive_forecast_stats(df: pd.DataFrame, last_n=52) -> ForecastResult:
    """Baseline: demand ~ Normal(mean, sd) estimated from the last N weeks."""
    tail = df.tail(last_n)
    mu = float(tail["demand_qty"].mean())
    sd = float(tail["demand_qty"].std(ddof=1)) if len(tail) > 1 else 0.0
    return ForecastResult(mean_weekly=mu, sd_weekly=sd, horizon_weeks=1)


def ensure_raw_exists(raw_dir: Path, seed=42) -> Path:
    """If no raw file exists, create one synthetic dataset."""
    raw_path = raw_dir / "synthetic_weekly_demand.csv"
    if not raw_path.exists():
        df = generate_synthetic_weekly(
            n_weeks=156, level=200, season_amp=30, noise_sd=20, seed=seed
        )
        raw_dir.mkdir(parents=True, exist_ok=True)
        df.to_csv(raw_path, index=False)
    return raw_path


def load_raw(raw_path: Path) -> pd.DataFrame:
    return pd.read_csv(raw_path, parse_dates=["date"])
