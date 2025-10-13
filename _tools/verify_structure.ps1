# === VERIFY PORTFOLIO STRUCTURE ===
cd "C:\Users\beall\OneDrive\Documents\Portfolio"

Write-Host "`n===== PORTFOLIO STRUCTURE CHECK =====" -ForegroundColor Cyan

# --- Core Domains ---
if (Test-Path "Core") {
    Write-Host "`n📊 CORE DOMAINS:" -ForegroundColor Yellow
    Get-ChildItem Core -Directory | ForEach-Object {
        Write-Host ("  - " + $_.Name) -ForegroundColor White
        Get-ChildItem $_.FullName -Directory | ForEach-Object {
            Write-Host ("       • " + $_.Name) -ForegroundColor DarkGray
        }
    }
} else { Write-Host "No Core directory found!" -ForegroundColor Red }

# --- Enablers ---
if (Test-Path "Enablers") {
    Write-Host "`n🧩 ENABLERS (Three-Layer Structure):" -ForegroundColor Yellow
    Get-ChildItem Enablers -Directory | ForEach-Object {
        Write-Host ("  - " + $_.Name) -ForegroundColor Green
        Get-ChildItem $_.FullName -Directory | ForEach-Object {
            Write-Host ("       • " + $_.Name) -ForegroundColor White
            Get-ChildItem $_.FullName -Directory | ForEach-Object {
                Write-Host ("           ▪ " + $_.Name) -ForegroundColor DarkGray
            }
        }
    }
} else { Write-Host "No Enablers directory found!" -ForegroundColor Red }

# --- Docs ---
if (Test-Path "docs") {
    Write-Host "`n📘 DOCUMENTATION:" -ForegroundColor Yellow
    Get-ChildItem docs -File | ForEach-Object {
        Write-Host ("  - " + $_.Name) -ForegroundColor White
    }
} else { Write-Host "No docs directory found!" -ForegroundColor Red }

Write-Host "`n===== END OF STRUCTURE CHECK =====`n" -ForegroundColor Cyan
