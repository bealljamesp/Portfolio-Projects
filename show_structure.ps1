param(
  [int]$DefaultDepth = 2,
  [int]$EnablerDepth = 4,
  [switch]$IncludeFilesAtEnablerLeaf,
  [switch]$SaveTxt,
  [string[]]$Exclude = @(
    '.git','_archive','_reports','.github','.venv','.conda',
    'node_modules','__pycache__','.ipynb_checkpoints'
  )
)

$root = (Get-Location).Path
$rootName = Split-Path -Leaf $root
$lines = New-Object System.Collections.Generic.List[string]
$lines.Add("[${rootName}]")
$lines.Add("+-- $rootName")

function Test-Excluded {
  param([string]$Rel, [string[]]$Patterns)
  foreach ($p in $Patterns) {
    if ($Rel -like "*\$p\*" -or $Rel -like "*$p*") { return $true }
  }
  return $false
}

# Get all directories once
$dirs = Get-ChildItem -Directory -Recurse -Force -ErrorAction SilentlyContinue |
        Sort-Object FullName

foreach ($d in $dirs) {
  $rel = $d.FullName.Substring($root.Length) -replace '^[\\/]+',''
  if (!$rel) { continue }
  if (Test-Excluded -Rel $rel -Patterns $Exclude) { continue }

  $depth = ($rel -split '[\\/]').Count
  $isEnabler = $rel -like "Enablers*"
  $allowedDepth = if ($isEnabler) { $EnablerDepth } else { $DefaultDepth }

  if ($depth -le $allowedDepth) {
    $indent = ("|  " * ($depth - 1))
    $lines.Add("$indent+-- $($d.Name)")

    # Optionally list files at the Enablers leaf depth (non-recursive)
    if ($IncludeFilesAtEnablerLeaf -and $isEnabler -and $depth -eq $EnablerDepth) {
      Get-ChildItem -LiteralPath $d.FullName -File -Force -ErrorAction SilentlyContinue |
        Sort-Object Name |
        ForEach-Object {
          $lines.Add("$indent|  - $($_.Name)")
        }
    }
  }
}

# Print to console
$lines | ForEach-Object { Write-Host $_ }

# Optionally save to _reports
if ($SaveTxt) {
  $reports = Join-Path $root "_reports"
  if (-not (Test-Path $reports)) { New-Item -Type Directory -Path $reports | Out-Null }
  $stamp = Get-Date -Format "yyyyMMdd_HHmmss"
  $outPath = Join-Path $reports "tree_$stamp.txt"
  $lines | Out-File -FilePath $outPath -Encoding UTF8
  Write-Host "`nSaved to: $outPath"
}
