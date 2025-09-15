<#
.SYNOPSIS
  Reorganize portfolio folders into a clean structure (ai/, msaba/, logistics/, scm_ai/).

.DESCRIPTION
  Moves existing folders (e.g., ai-01_*, log-02-*) into new grouped directories with normalized names.
  Dry-run by default. Use -Perform to actually move files.

.PARAMETER Root
  Root path of the portfolio repo (default: current directory).

.PARAMETER Perform
  Switch to perform the moves; otherwise shows planned actions only.

.EXAMPLE
  .\reorg_portfolio.ps1 -Root "C:\Users\beall\OneDrive\Documents\Resume\Portfolio" -Perform -Verbose
#>

param(
  [string]$Root = ".",
  [switch]$Perform
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function Ensure-Dir {
  param([string]$Path)
  if (!(Test-Path $Path)) {
    Write-Verbose "Creating dir: $Path"
    if ($Perform) { New-Item -ItemType Directory -Force -Path $Path | Out-Null }
  }
}

# Map current names -> destination subpaths
$map = @{
  "msaba-01-churn-prediction-logit"            = "msaba\01_churn_prediction_logit"
  "msaba-02-ab-testing-experiment-design"      = "msaba\02_ab_testing_experiment_design"
  "msaba-03-time-series-forecasting"           = "msaba\03_time_series_forecasting"
  "msaba-04-pricing-product-mix-optimization"  = "msaba\04_pricing_product_mix_optimization"

  "log-01-sql-python-excel-kpis-dashboard"     = "logistics\01_sql_python_excel_kpis_dashboard"
  "log-02-forecasting-inventory-policies"      = "logistics\02_forecasting_inventory_policies"
  "log-03-network-optimization-monte-carlo"    = "logistics\03_network_optimization_monte_carlo"

  "ai-01_Customer_Churn_ExplainableAI"         = "ai\01_customer_churn_explainableai"
  "ai-02_AI_Forecasting_Retail_Demand"         = "ai\02_ai_forecasting_retail_demand"
  "ai-03_Computer_Vision_Logistics"            = "ai\03_computer_vision_logistics"
  "ai-04_GenerativeAI_SupplyChainDocs"         = "ai\04_generativeai_supplychaindocs"

  "scm-01_AI_Inventory_Optimization"           = "scm_ai\01_ai_inventory_optimization"
  "scm-02_Digital_Twin_SupplyChain"            = "scm_ai\02_digital_twin_supplychain"
}

# Create top-level groups
foreach ($group in @("ai","msaba","logistics","scm_ai")) {
  Ensure-Dir -Path (Join-Path $Root $group)
}

# Plan & execute
$planned = @()
foreach ($srcName in $map.Keys) {
  $src = Join-Path $Root $srcName
  if (Test-Path $src) {
    $dst = Join-Path $Root $map[$srcName]
    Ensure-Dir -Path (Split-Path $dst -Parent)
    $planned += [PSCustomObject]@{ From=$src; To=$dst }
    Write-Host ("MOVE: {0}  ->  {1}" -f $srcName, $map[$srcName])
    if ($Perform) {
      try {
        Move-Item -Path $src -Destination $dst -Force -Verbose
      } catch {
        Write-Warning "Failed to move $src => $dst : $_"
      }
    }
  } else {
    Write-Verbose "SKIP (not found): $srcName"
  }
}

# Write summary
Write-Host ""
Write-Host "Planned moves:"
$planned | Format-Table -AutoSize

Write-Host ""
if ($Perform) {
  Write-Host "✅ Reorg complete."
} else {
  Write-Host "Dry run only. Re-run with -Perform to execute."
}
