param([string]$Mode="local",[int]$Port=8001)
$env:VERIFY_MODE = $Mode
conda activate ai-scm-portfolio
python -m uvicorn services.verify_api.main:app --host 127.0.0.1 --port $Port
