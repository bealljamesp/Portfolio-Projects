param(
  [Parameter(Mandatory = $true)][string]$NotebookPath,
  [Parameter(Mandatory = $true)][string]$SanityCellPath
)

if (-not (Test-Path $NotebookPath)) { Write-Error "Notebook not found: $NotebookPath"; exit 1 }
if (-not (Test-Path $SanityCellPath)) { Write-Error "Sanity cell file not found: $SanityCellPath"; exit 1 }

# Load notebook JSON
$nbJson = Get-Content -Raw -LiteralPath $NotebookPath | ConvertFrom-Json

# Marker used to detect an existing cell
$Marker = "# --- Sanity Check Cell (inline, self-contained) ---"

# Check for existing sanity cell
$exists = $false
foreach ($cell in $nbJson.cells) {
  if ($cell.cell_type -eq "code") {
    $src = ($cell.source -join "")
    if ($src -like "*$Marker*") { $exists = $true; break }
  }
}

if ($exists) {
  Write-Host "Sanity Check cell already present. No changes made." -ForegroundColor Yellow
  exit 0
}

# Load sanity cell code from file and ensure it has the marker at top
$code = Get-Content -Raw -LiteralPath $SanityCellPath
if ($code -notlike "*$Marker*") {
  $code = "$Marker`n$code"
}

# Create a new code cell object
$sanityCell = [pscustomobject]@{
  cell_type = "code"
  metadata  = @{}
  source    = ($code -split "`n")
  outputs   = @()
  execution_count = $null
}

# Decide insertion index:
# If first cell is markdown (title/intro), insert AFTER it; otherwise prepend
$insertIndex = 0
if ($nbJson.cells.Count -gt 0 -and $nbJson.cells[0].cell_type -eq "markdown") {
  $insertIndex = 1
}

# Insert the sanity cell
$pre  = @()
$post = @()
if ($insertIndex -gt 0) { $pre  = $nbJson.cells[0..($insertIndex-1)] }
if ($insertIndex -lt $nbJson.cells.Count) { $post = $nbJson.cells[$insertIndex..($nbJson.cells.Count-1)] }

$nbJson.cells = @($pre + @($sanityCell) + $post)

# Write updated notebook
$nbJson | ConvertTo-Json -Depth 200 | Set-Content -LiteralPath $NotebookPath -Encoding UTF8
Write-Host "Inserted Sanity Check cell into $NotebookPath (index $insertIndex)" -ForegroundColor Green
