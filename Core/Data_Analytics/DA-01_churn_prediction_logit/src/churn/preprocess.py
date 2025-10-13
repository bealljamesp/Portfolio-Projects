from pathlib import Path
from typing import Tuple, Iterable
import pandas as pd

TARGET_CANDIDATES: Iterable[str] = ("churned", "churn_60d", "Churn")


def load_churn_data(root: Path) -> pd.DataFrame:
    raw = root / "data" / "raw"

    customers = pd.read_csv(raw / "customers.csv", parse_dates=["signup_dt"])
    interactions = pd.read_csv(raw / "interactions.csv")
    labels = None
    # Try separate labels file; if not present, assume target lives in customers/interactions
    labels_path = raw / "churn_labels.csv"
    if labels_path.exists():
        labels = pd.read_csv(labels_path)

    # Merge
    df = customers.merge(interactions, on="customer_id", how="left")
    if labels is not None:
        df = df.merge(labels, on="customer_id", how="left")

    # Drop stray "Unnamed" columns from sloppy CSVs
    df = df.loc[:, ~df.columns.str.startswith("Unnamed")].copy()

    # Derived features
    today = pd.Timestamp("today").normalize()
    if "signup_dt" in df.columns:
        df["tenure_days"] = (today - df["signup_dt"]).dt.days
        df["tenure_months"] = df["tenure_days"] / 30.0

    # Standardize target to 'churned'
    if "churned" not in df.columns:
        found = next((c for c in TARGET_CANDIDATES if c in df.columns), None)
        if not found:
            raise KeyError(
                f"No churn target found. Expected one of {list(TARGET_CANDIDATES)}."
            )
        df.rename(columns={found: "churned"}, inplace=True)

    df["churned"] = pd.to_numeric(df["churned"], errors="coerce").fillna(0).astype(int)

    # Optional dtype normalization
    if "region" in df.columns:
        df["region"] = df["region"].astype("category")

    # Ensure expected numeric columns exist (create if missing)
    for col in [
        "logins_last_30d",
        "avg_session_min",
        "support_tickets_last_90d",
        "nps_score",
    ]:
        if col not in df.columns:
            df[col] = 0

    return df
