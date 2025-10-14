param(
  [string]$Root = (Get-Location).Path,
  [string]$ReportsDirName = "_reports"
)

# Ensure reports dir
$ReportsDir = Join-Path $Root $ReportsDirName
if (-not (Test-Path $ReportsDir)) { New-Item -Type Directory -Path $ReportsDir | Out-Null }

$stamp     = Get-Date -Format "yyyyMMdd_HHmmss"
$csvInv    = Join-Path $ReportsDir "portfolio_inventory_$stamp.csv"
$txtTree   = Join-Path $ReportsDir "portfolio_tree_$stamp.txt"
$csvRename = Join-Path $ReportsDir "rename_candidates_$stamp.csv"

# 1) Full inventory (files + folders), with depth
Get-ChildItem -Recurse -Force -File -Directory |
  Select-Object `
    FullName, PSIsContainer, Name, Extension, Length, LastWriteTime,
    @{n="Depth";e={
      $rel = $_.FullName.Substring($Root.Length) -replace '^[\\/]+',''
      if ([string]::IsNullOrWhiteSpace($rel)) { 0 } else { ($rel -split '[\\\/]').Count }
    }} |
  Export-Csv -NoTypeInformation -Encoding UTF8 -Path $csvInv

# 2) ASCII tree (folders only)
function New-AsciiTree {
  param([string]$Path)

  $dirs = Get-ChildItem -Directory -Recurse -Force -ErrorAction SilentlyContinue |
          Sort-Object FullName

  $rootName = Split-Path -Leaf $Path
  $lines = @()
  $lines += "[${rootName}]"
  $lines += "+-- $rootName"

  foreach ($d in $dirs) {
    $rel = $d.FullName.Substring($Path.Length) -replace '^[\\/]+',''
    if ($rel -eq "") { continue }
    $depth = ($rel -split '[\\\/]').Count
    $indent = ("|  " * ($depth - 1))
    $lines += "$indent+-- $($d.Name)"
  }

  return $lines
}

New-AsciiTree -Path $Root | Out-File -Encoding UTF8 -FilePath $txtTree

# 3) Naming audit for top-level project directories
#    Convention: PREFIX-NN_slug   (e.g., SCM-01_forecasting_inventory_policies)
$allowedPrefixes = @('SCM','DA','AI','BC')
$strictPattern   = '^(?<prefix>[A-Za-z]{2,3})-(?<num>\d{1,2})_(?<slug>[A-Za-z0-9_]+)$'
$loosePattern    = '^(?<pfx>[A-Za-z]{2,3})[\-_ ](?<n>\d{1,2})[\-_ ](?<rest>.+)$'

# Top-level dirs to ignore
$ignoreTop = @('_archive','_reports','enabler','core','.git','.github','.venv','.conda')

$topDirs = Get-ChildItem -Directory $Root | Where-Object {
  $_.Name -notin $ignoreTop -and ($_.Name -notmatch '^\.')
}

$rows = foreach ($d in $topDirs) {
  $name   = $d.Name
  $isMatch = $false
  $prefix = $null
  $num    = $null
  $slug   = $null

  if ($name -match $strictPattern) {
    $prefix = $Matches['prefix'].ToUpper()
    $num    = [int]$Matches['num']
    $slug   = ($Matches['slug']).ToLower()
    $isMatch = $true
  } elseif ($name -match $loosePattern) {
    $prefix = $Matches['pfx'].ToUpper()
    $num    = [int]$Matches['n']
    $slug   = ($Matches['rest'] -replace '[^A-Za-z0-9_]+','_').ToLower().TrimEnd('_')
    $isMatch = $true
  }

  $needsRename = $false
  $proposed    = $null
  $allowed     = ($allowedPrefixes -contains $prefix)

  if ($isMatch -and $allowed) {
    $normNum = '{0:00}' -f $num
    $target  = "$prefix-$normNum" + '_' + $slug
    if ($target -ne $name) {
      $proposed = Join-Path $d.Parent.FullName $target
      $needsRename = $true
    }
  }

  [pscustomobject]@{
    CurrentPath    = $d.FullName
    CurrentName    = $name
    ParsedPrefix   = $prefix
    ParsedNum      = $num
    ParsedSlug     = $slug
    AllowedPrefix  = $allowed
    MatchesPattern = $isMatch
    NeedsRename    = $needsRename
    ProposedPath   = $proposed
  }
}

$rows | Sort-Object @{Expression = "NeedsRename"; Descending = $true}, @{Expression = "CurrentName"; Descending = $false} | Export-Csv -NoTypeInformation -Encoding UTF8 -Path $csvRename

  Export-Csv -NoTypeInformation -Encoding UTF8 -Path $csvRename

Write-Host "Inventory CSV: $csvInv"
Write-Host "Tree TXT:      $txtTree"
Write-Host "Rename CSV:    $csvRename"
