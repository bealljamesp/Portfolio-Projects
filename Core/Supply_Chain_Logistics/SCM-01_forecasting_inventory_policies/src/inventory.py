from __future__ import annotations
from dataclasses import dataclass
from math import sqrt
from scipy.stats import norm  # make sure scipy is in your env

# conda install scipy   (or)   pip install scipy


@dataclass
class Policy:
    Q: float  # order quantity (EOQ)
    s: float  # reorder point
    z: float  # safety factor
    ss: float  # safety stock units


def eoq(D_annual: float, K: float, h_rate: float, unit_cost: float) -> float:
    """
    Classic EOQ: sqrt(2 * K * D / H), where H = h_rate * unit_cost (annual holding per unit).
    D_annual: units/year, K: order cost, h_rate: annual % of unit cost, unit_cost: $
    """
    H = h_rate * unit_cost
    return sqrt((2.0 * K * D_annual) / max(H, 1e-12))


def safety_stock(
    mu_week: float, sd_week: float, L_days: float, service: float
) -> tuple[float, float]:
    """
    Approx safety stock under Normal: z * sigma_L.
    Convert weekly stats to lead-time stats assuming iid weekly demand.
    """
    z = norm.ppf(service)
    L_weeks = L_days / 7.0
    sigma_L = sd_week * (L_weeks**0.5)  # rough: sd scales with sqrt(time)
    ss = z * sigma_L
    return z, ss


def reorder_point(mu_week: float, L_days: float, ss: float) -> float:
    """s = mean demand over L + safety stock."""
    L_weeks = L_days / 7.0
    return mu_week * L_weeks + ss


def build_policy(
    mu_week: float,
    sd_week: float,
    L_days: float,
    service: float,
    D_annual: float,
    K: float,
    h_rate: float,
    unit_cost: float,
) -> Policy:
    Q = eoq(D_annual=D_annual, K=K, h_rate=h_rate, unit_cost=unit_cost)
    z, ss = safety_stock(mu_week, sd_week, L_days, service)
    s = reorder_point(mu_week, L_days, ss)
    return Policy(Q=Q, s=s, z=z, ss=ss)
