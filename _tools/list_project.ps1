<#
.SYNOPSIS
    Displays a clean, emoji-styled directory tree for any project folder.
.DESCRIPTION
    Pass the target project path (e.g., Core\Supply_Chain_Logistics\SCM-01_forecasting_inventory_policies).
    Shows nested structure up to MaxDepth (default = 6).
.EXAMPLE
    .\_tools\list_project.ps1 -Path .\Core\Supply_Chain_Logistics\SCM-01_forecasting_inventory_policies
#>

param(
    [Parameter(Mandatory = $true)][string]$Path,
    [int]$MaxDepth = 6
)

if (-not (Test-Path $Path)) {
    Write-Error "❌ Path not found: $Path"
    exit 1
}

$Root = (Resolve-Path $Path).Path
Write-Host ""
Write-Host "===== DIRECTORY STRUCTURE =====" -ForegroundColor Cyan
Write-Host "Root: $Root`n"

function Show-Tree {
    param(
        [string]$Base,
        [int]$Depth
    )

    if ($Depth -gt $MaxDepth) { return }

    $items = Get-ChildItem -LiteralPath $Base -Force | Sort-Object PSIsContainer, Name

    $items = $items | Where-Object {
        $_.Name -notmatch '^(__pycache__|\.ipynb_checkpoints)$'
    }

    foreach ($i in $items) {
        # Relative path and indentation
        $rel = $i.FullName.Substring($Root.Length).TrimStart('\')
        $indent = "  " * ($Depth - 1)

        if ($i.PSIsContainer) {
            Write-Host "$indent📁 $rel" -ForegroundColor Yellow
            Show-Tree -Base $i.FullName -Depth ($Depth + 1)
        }
        else {
            Write-Host "$indent  • $rel" -ForegroundColor Gray
        }
    }
}

Show-Tree -Base $Root -Depth 1

Write-Host "`n===== END OF STRUCTURE CHECK =====" -ForegroundColor Cyan
