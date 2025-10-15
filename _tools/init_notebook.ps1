param(
  [string]$ProjectPath = ".",
  [string[]]$Names = @("forecasting","inventory_policy","simulation","results_reflection")
)

$nbDir = Join-Path $ProjectPath "notebooks"
if (-not (Test-Path $nbDir)) { New-Item -ItemType Directory -Path $nbDir | Out-Null }

$sanity = @"
# --- Notebook Sanity Cell (standard) ---
import os, sys, platform, random, numpy as np, pandas as pd
from pathlib import Path
print("Python:", sys.version.split()[0], "| OS:", platform.system(), platform.release())
print("Conda env:", os.environ.get("CONDA_DEFAULT_ENV", "<unknown>"))
CANDIDATES = ["src", "data", "notebooks"]
here = Path.cwd()
root = here
for p in [here] + list(here.parents):
    if all((p / c).exists() for c in CANDIDATES):
        root = p; break
os.chdir(root); print("Working dir set to:", Path.cwd())
src = Path("src")
if src.exists() and str(src.resolve()) not in sys.path:
    sys.path.insert(0, str(src.resolve()))
    print("Added to PYTHONPATH:", src.resolve())
%load_ext autoreload
%autoreload 2
pd.set_option("display.max_rows", 50)
pd.set_option("display.max_columns", 100)
pd.options.display.float_format = "{:,.4f}".format
np.random.seed(42); random.seed(42)
import matplotlib.pyplot as plt
print("Libs ok: numpy={}, pandas={}, matplotlib={}".format(np.__version__, pd.__version__, plt.matplotlib.__version__))
"@

function New-NotebookJson {
  param([string]$title, [string]$firstCell)
  $obj = [ordered]@{
    "cells" = @(
      [ordered]@{
        "cell_type"="markdown"; "metadata"=@{}; "source"=@("# $title`n")
      },
      [ordered]@{
        "cell_type"="code"; "metadata"=@{}; "outputs"=@(); "execution_count"=$null;
        "source" = $firstCell -split "`r?`n"
      }
    )
    "metadata" = @{ "kernelspec" = @{ "display_name" = "Python (analytics_portfolio)"; "language"="python"; "name"="python3" } }
    "nbformat"=4; "nbformat_minor"=5
  }
  return ($obj | ConvertTo-Json -Depth 6)
}

$i = 1
foreach ($n in $Names) {
  $file = Join-Path $nbDir ("{0:00}_{1}.ipynb" -f $i, $n)
  if (-not (Test-Path $file)) {
    (New-NotebookJson -title ($n -replace '_',' ' | ForEach-Object { $_ }) -firstCell $sanity) |
      Out-File -Encoding UTF8 $file
    Write-Host "Created: $file"
  } else {
    Write-Host "Exists:  $file"
  }
  $i++
}
