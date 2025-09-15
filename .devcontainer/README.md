
# Dev Container for Portfolio

This folder provides a **VS Code Dev Container** so anyone can open this repo in a pre-configured environment (locally with Docker or in GitHub Codespaces).

## Setup Options

### Pip (default)
- Uses base image `mcr.microsoft.com/devcontainers/python:3.11`.
- Runs `pip install -r requirements.txt` if that file exists at repo root.

### Conda (optional)
If you want conda in-container:
1. Add the Miniconda feature in `devcontainer.json`.
2. Replace `postCreateCommand` with:
   ```json
   "postCreateCommand": "conda init bash && conda env create -f environment.yml && echo 'conda activate ai-scm-portfolio' >> ~/.bashrc"
   ```

## Usage
1. Install Docker + VS Code + Dev Containers extension.
2. Open the repo in VS Code → **Ctrl+Shift+P → Dev Containers: Reopen in Container**.
3. Container builds, dependencies install, and you're ready to run notebooks.

## Why Dev Containers?
- **Reproducibility**: same Python + deps on any machine.
- **Zero-setup sharing**: recruiters, collaborators, or Codespaces users can run immediately.
- **Isolation**: no conflict with your system Python installs.
