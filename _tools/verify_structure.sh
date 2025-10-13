#!/usr/bin/env bash
# =============================================
# Verify Portfolio Structure (Linux/macOS/WSL)
# =============================================

PORTFOLIO_DIR="$HOME/OneDrive/Documents/Portfolio"
if [ -d "$PWD/Core" ] && [ -d "$PWD/Enablers" ]; then
  PORTFOLIO_DIR="$PWD"
fi

echo ""
echo "===== PORTFOLIO STRUCTURE CHECK ====="
cd "$PORTFOLIO_DIR" || { echo "Portfolio directory not found!"; exit 1; }

# --- Core Domains ---
if [ -d "Core" ]; then
  echo ""
  echo "📊 CORE DOMAINS:"
  for dir in Core/*; do
    [ -d "$dir" ] || continue
    echo "  - $(basename "$dir")"
    for sub in "$dir"/*; do
      [ -d "$sub" ] || continue
      echo "       • $(basename "$sub")"
    done
  done
else
  echo "No Core directory found!"
fi

# --- Enablers ---
if [ -d "Enablers" ]; then
  echo ""
  echo "🧩 ENABLERS (Three-Layer Structure):"
  for layer in Enablers/*; do
    [ -d "$layer" ] || continue
    echo "  - $(basename "$layer")"
    for sub in "$layer"/*; do
      [ -d "$sub" ] || continue
      echo "       • $(basename "$sub")"
      for deep in "$sub"/*; do
        [ -d "$deep" ] || continue
        echo "           ▪ $(basename "$deep")"
      done
    done
  done
else
  echo "No Enablers directory found!"
fi

# --- Docs ---
if [ -d "docs" ]; then
  echo ""
  echo "📘 DOCUMENTATION:"
  for f in docs/*.md; do
    [ -e "$f" ] || continue
    echo "  - $(basename "$f")"
  done
else
  echo "No docs directory found!"
fi

echo ""
echo "===== END OF STRUCTURE CHECK ====="
echo ""
