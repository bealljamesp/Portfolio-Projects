# bootstrap_sqlite.py (robust header detection)
import os, json, sqlite3, hashlib, requests, re
from pathlib import Path
import pandas as pd

# --- Locate portfolio root so paths work from anywhere ---
PORTFOLIO_ROOT = next(
    p
    for p in [Path.cwd(), *Path.cwd().parents]
    if (p / "Blockchain/common/utils/hash_anchor.py").exists()
)

PROJECT = PORTFOLIO_ROOT / "Logistics" / "LOG-04_TamperEvident_Warehouse"
DATA = PROJECT / "data"
DB = PROJECT / "warehouse.db"

CSV = DATA / "demo_shipments.csv"
MANIFEST = PORTFOLIO_ROOT / "Blockchain/common/notebooks/demo_shipments.manifest.json"

if not CSV.exists():
    raise FileNotFoundError(f"Missing CSV: {CSV}")
if not MANIFEST.exists():
    raise FileNotFoundError(f"Missing manifest: {MANIFEST}")

dataset_hash = json.loads(MANIFEST.read_text(encoding="utf-8"))["dataset_hash"]


# --- 0) Helpers: normalize & find columns ---
def norm(s: str) -> str:
    # lowercase, remove non-alphanum
    return re.sub(r"[^a-z0-9]", "", s.strip().lower())


def find_col(orig_cols, candidates):
    """
    Return the ORIGINAL column name matching any of the candidate names
    after normalization; else None.
    """
    nmap = {norm(c): c for c in orig_cols}
    for cand in candidates:
        c = norm(cand)
        if c in nmap:
            return nmap[c]
    # try contains-match fallback (e.g., 'tracking' in 'trackingnumber')
    for k, v in nmap.items():
        if any(norm(cand) in k for cand in candidates):
            return v
    return None


# --- 1) Create DB & load raw_shipments ---
if DB.exists():
    DB.unlink()  # fresh demo DB
con = sqlite3.connect(DB)
cur = con.cursor()

df = pd.read_csv(CSV)
orig_cols = list(df.columns)
df.columns = [c.strip() for c in df.columns]  # keep original but trimmed for SQL

# Save raw as-is (important for reproducible hashing)
df.to_sql("raw_shipments", con, index=False)


# --- 2) stage_ship_rowhash: deterministic row hash (sorted columns, '|' join) ---
def row_digest(row: pd.Series) -> str:
    keys = sorted(row.index)
    payload = "|".join(str(row[k]) for k in keys).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


ship = df.copy()
ship["row_hash"] = ship.apply(row_digest, axis=1)

# Detect a shipment key for staging/joining (do NOT add it to hashing)
shipment_key = find_col(
    orig_cols,
    [
        "ShipmentID",
        "Shipment Id",
        "shipment_id",
        "shipmentid",
        "TrackingNumber",
        "tracking_number",
        "tracking",
        "Waybill",
        "ConsignmentID",
        "OrderID",
        "LoadID",
        "Load Id",
        "Reference",
    ],
)
if shipment_key is None:
    # Fall back to row number as a staging key ONLY (not included in hashing)
    ship.insert(0, "__RowNumber", range(1, len(ship) + 1))
    staging_cols = ["__RowNumber", "row_hash"]
    staging_name = "__RowNumber"  # for messages
else:
    staging_cols = [shipment_key, "row_hash"]
    staging_name = shipment_key

ship[staging_cols].to_sql("stage_ship_rowhash", con, index=False)

# --- 3) KPI build (cold-chain metrics for your schema) ---

# Explicit overrides to lock to your actual columns
OVERRIDES = {
    "shipment_key": "shipment_id",
    "product": "gtin",
    "case": "case_id",
    "temp": "temp_c",
}

shipment_key = OVERRIDES["shipment_key"]
product_col = OVERRIDES["product"]
case_col = OVERRIDES["case"]
temp_col = OVERRIDES["temp"]

missing = [k for k, v in OVERRIDES.items() if v not in df.columns]
if missing:
    raise SystemExit(
        f"Missing expected columns for KPI build: {missing}. "
        f"Found columns: {list(df.columns)}"
    )

# Build KPIs
kpi = df.copy()
# Ensure temp is numeric
kpi[temp_col] = pd.to_numeric(kpi[temp_col], errors="coerce")

# Base KPI grain: by shipment_id + gtin (product)
group_cols = [shipment_key, product_col]

# Core measures
kpi_ship_product = (
    kpi.groupby(group_cols, dropna=False)
    .agg(
        avg_temp_c=(temp_col, "mean"),
        min_temp_c=(temp_col, "min"),
        max_temp_c=(temp_col, "max"),
        readings=(temp_col, "size"),
    )
    .reset_index()
)

# Optional: cold-chain out-of-range percent (adjust band as needed)
LOW, HIGH = 2.0, 8.0
oob = (
    kpi.assign(oob=((kpi[temp_col] < LOW) | (kpi[temp_col] > HIGH)).astype("int"))
    .groupby(group_cols, dropna=False)["oob"]
    .mean()
    .rename("pct_oob")
    .reset_index()
)
kpi_ship_product = kpi_ship_product.merge(oob, on=group_cols, how="left")

# Write KPIs
kpi_ship_product.to_sql("kpi_ship_product", con, index=False, if_exists="replace")

# Also publish a simple “shipment summary” table (one row per shipment)
kpi_shipment = (
    kpi_ship_product.groupby([shipment_key], dropna=False)
    .agg(
        avg_temp_c=("avg_temp_c", "mean"),
        max_temp_c=("max_temp_c", "max"),
        min_temp_c=("min_temp_c", "min"),
        readings=("readings", "sum"),
        pct_oob=("pct_oob", "mean"),
    )
    .reset_index()
)
kpi_shipment.to_sql("kpi_shipment_summary", con, index=False, if_exists="replace")

# --- 4) KPI + provenance: attach dataset_hash ---
kpi_shipment["dataset_hash"] = dataset_hash
kpi_shipment.to_sql("kpi_shipment_provenance", con, index=False, if_exists="replace")
kpi_rows = len(kpi_shipment)

# --- 5) Verify dataset_hash via FastAPI and log into proofs_dataset ---
BASE = os.getenv("VERIFY_API_BASE", "http://127.0.0.1:8001")
resp = requests.get(f"{BASE}/verify", params={"hash": dataset_hash}, timeout=8)
resp.raise_for_status()
ver = resp.json()

cur.execute(
    """
CREATE TABLE IF NOT EXISTS proofs_dataset (
  dataset_hash TEXT PRIMARY KEY,
  verified     INTEGER,
  reason       TEXT,
  verified_at  TEXT DEFAULT (datetime('now'))
)
"""
)
cur.execute("DELETE FROM proofs_dataset WHERE dataset_hash = ?", (dataset_hash,))
cur.execute(
    "INSERT INTO proofs_dataset(dataset_hash, verified, reason) VALUES (?, ?, ?)",
    (dataset_hash, int(bool(ver.get("ok"))), ver.get("reason")),
)
con.commit()

# --- Summary & hints ---
print("DB:", DB)
print("dataset_hash:", dataset_hash)
print("verify:", ver)
print("staging key used:", staging_name)
print("kpi rows:", kpi_rows)
con.close()
