param(
  [string]$Root = ".",
  [string]$Project = "Core/Supply_Chain_Logistics/SCM-01_forecasting_inventory_policies",
  [switch]$CreateMissingSpec,
  [switch]$RunPytest,
  [switch]$ScanCore,
  [string]$Python = "python"
)

$script = Join-Path $Root "_tools/check_portfolio_integrity.py"
if (-not (Test-Path $script)) {
  Write-Error "Integrity script not found: $script"
  exit 1
}

$flags = @("--root", $Root)
if ($ScanCore) {
  $flags += @("--scan-core")
} else {
  $flags += @("--project", $Project)
}
if ($CreateMissingSpec) { $flags += @("--create-missing-spec") }
if ($RunPytest) { $flags += @("--run-pytest") }

& $Python $script @flags
exit $LASTEXITCODE
