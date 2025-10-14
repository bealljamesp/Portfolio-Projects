<# 
open_project.ps1
Usage:
  .\open_project.ps1 <projectKey> [-Env <condaEnv>] [-Notebook <relativePath>]

Examples:
  .\open_project.ps1 SCM-01
  .\open_project.ps1 SCM-01 -Env analytics_portfolio -Notebook notebooks\01_scm01_forecast_policy_sim.ipynb

Notes:
- Set $Env:PORTFOLIO_ROOT once (machine-specific) to your Portfolio root path.
- Edit $Projects map below to add/remove projects without changing usage.
#>

param(
  [Parameter(Mandatory=$true, Position=0)]
  [string]$ProjectKey,
  [string]$Env = "analytics_portfolio",
  [string]$Notebook
)

# ---- 0) Resolve Portfolio root ----
if (-not $Env:PORTFOLIO_ROOT) {
  Write-Host "❗ Set PORTFOLIO_ROOT first, e.g.:" -ForegroundColor Yellow
  Write-Host '$Env:PORTFOLIO_ROOT = "C:\Users\beall\OneDrive\Documents\Portfolio"' -ForegroundColor Yellow
  exit 1
}
$Root = $Env:PORTFOLIO_ROOT

# ---- 1) Project registry (keys → relative paths) ----
$Projects = @{
  # Core → Supply Chain & Logistics
  "SCM-01" = "Core\Supply_Chain_Logistics\SCM-01_forecasting_inventory_policies"
  "SCM-02" = "Core\Supply_Chain_Logistics\SCM-02_network_optimization_montecarlo"

  # Analytics (examples you listed)
  "DA-01"  = "Core\Analytics\DA-01_churn_prediction_logit"
  "DA-03"  = "Core\Analytics\DA-03_time_series_forecasting"

  # AI
  "AI-02"  = "Core\AI\AI-02_ai_forecasting_retail_demand"
  "AI-04"  = "Core\AI\AI-04_generativeai_supplychaindocs"

  # Blockchain
  "BLK-03" = "Core\Blockchain\BLK-03_pharma_serialization_dscsa_sim"
}

if (-not $Projects.ContainsKey($ProjectKey)) {
  Write-Host "❌ Unknown project key: $ProjectKey" -ForegroundColor Red
  Write-Host "Available keys: $($Projects.Keys -join ', ')" -ForegroundColor Yellow
  exit 1
}

$ProjectPath = Join-Path $Root $Projects[$ProjectKey]
if (-not (Test-Path $ProjectPath)) {
  Write-Host "❌ Project path not found:" $ProjectPath -ForegroundColor Red
  exit 1
}

# ---- 2) Ensure 'conda' is available in this PowerShell session ----
# If Conda wasn't initialized for PowerShell, try to import it (Miniconda default path)
if (-not (Get-Command conda -ErrorAction SilentlyContinue)) {
  $possibleProfile = "C:\Users\beall\miniconda3\shell\condabin\conda-hook.ps1"
  if (Test-Path $possibleProfile) {
    & $possibleProfile | Out-Null
  }
}

if (-not (Get-Command conda -ErrorAction SilentlyContinue)) {
  Write-Host "❌ 'conda' command not found. Initialize Conda for PowerShell:" -ForegroundColor Red
  Write-Host "   conda init powershell" -ForegroundColor Yellow
  exit 1
}

# ---- 3) Activate the desired Conda environment ----
Write-Host "🔧 Activating Conda env:" $Env -ForegroundColor Cyan
conda activate $Env

# ---- 4) Change directory to the project root ----
Set-Location $ProjectPath

# ---- 5) Launch VS Code workspace ----
if (-not (Get-Command code -ErrorAction SilentlyContinue)) {
  Write-Host "❌ 'code' CLI not found. In VS Code, run: 'Shell Command: Install 'code' command in PATH'." -ForegroundColor Red
  exit 1
}

Write-Host "🚀 Opening VS Code in workspace:" $ProjectPath -ForegroundColor Green
# Open the workspace folder
code .

# ---- 6) Optional: open a specific notebook (after Code starts) ----
if ($Notebook) {
  $nbPath = Join-Path $ProjectPath $Notebook
  if (Test-Path $nbPath) {
    Start-Sleep -Milliseconds 500
    code $nbPath
  } else {
    Write-Host "⚠️ Notebook not found:" $nbPath -ForegroundColor Yellow
  }
}

# ---- 7) Helpful diagnostics ----
Write-Host ""
Write-Host "Summary:" -ForegroundColor Gray
Write-Host ("  Env          : {0}" -f $Env)
Write-Host ("  Workspace    : {0}" -f $ProjectPath)
Write-Host ("  Notebook     : {0}" -f ($(if ($Notebook) { $Notebook } else { "(none)" })))
Write-Host ("  Python exe   : {0}" -f (& python -c "import sys; print(sys.executable)"))
Write-Host ("  CWD (shell)  : {0}" -f (Get-Location).Path)
