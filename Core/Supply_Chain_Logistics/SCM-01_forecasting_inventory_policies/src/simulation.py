from __future__ import annotations
from dataclasses import dataclass
import numpy as np


@dataclass
class SimResult:
    service_level: float
    avg_inventory: float
    stockouts: int
    orders_placed: int


def simulate_sQ(
    demand: np.ndarray,
    policy_s: float,
    policy_Q: float,
    lead_time_days=14,
    review_period_days=7,
    initial_inventory=None,
    seed=42,
) -> SimResult:
    """
    Simple periodic-review (R, s, Q) sim with weekly demand.
    - Review every `review_period_days` (default weekly).
    - If on-hand <= s at review, place order of Q. Arrives after lead_time_days.
    """
    rng = np.random.default_rng(seed)
    weeks = len(demand)
    on_hand = float(
        initial_inventory if initial_inventory is not None else policy_s + policy_Q
    )
    pipeline = []  # list of (arrival_week, qty)
    stockouts = 0
    orders = 0
    inv_hist = []
    fulfilled_hist = 0

    L_weeks = max(1, int(round(lead_time_days / 7.0)))
    for t in range(weeks):
        # Receive arrivals
        arrivals = sum(q for w, q in pipeline if w == t)
        pipeline = [(w, q) for w, q in pipeline if w != t]
        on_hand += arrivals

        # Satisfy demand
        d = float(demand[t])
        shipped = min(on_hand, d)
        on_hand -= shipped
        if shipped < d:
            stockouts += 1
        fulfilled_hist += shipped
        inv_hist.append(on_hand)

        # Periodic review at the end of week
        if (t + 1) % max(1, int(round(review_period_days / 7.0))) == 0:
            if on_hand <= policy_s:
                pipeline.append((t + L_weeks, policy_Q))
                orders += 1

    avg_inv = float(np.mean(inv_hist)) if inv_hist else 0.0
    service = fulfilled_hist / max(1e-9, float(np.sum(demand)))
    return SimResult(
        service_level=service,
        avg_inventory=avg_inv,
        stockouts=stockouts,
        orders_placed=orders,
    )
