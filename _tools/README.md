# 🧰 Portfolio Developer Tools

This folder contains scripts and notes for maintaining the **Analytics & Decision Intelligence Portfolio** across systems.  
All utilities here are cross-platform and designed for reproducibility.

---

## ⚙️ Structure Verification

| Script | Environment | Description |
|---------|--------------|--------------|
| `verify_structure.ps1` | 💻 Windows (PowerShell) | Verifies the portfolio directory tree and highlights any missing folders. |
| `verify_structure.sh` | 🐧 Linux / macOS / WSL (Bash) | Equivalent verifier for Unix-style environments. |

**Usage**
```powershell
# Windows PowerShell
.\_tools\verify_structure.ps1

# Linux / macOS / WSL
./_tools/verify_structure.sh
```

## Conda Environment Maintenance

### Create Environment (from root)
```
conda env create -f environment.yml
conda activate analytics_portfolio
```
### Register Environment for Jupyter
```
python -m ipykernel install --user --name analytics_portfolio --display-name "Python (analytics_portfolio)"
```
### Update Environment After Editing environment.yml
```
conda env update -f environment.yml --prune
```