# FastAPI Jobs API

Enqueue background work and poll job status.

Local FastAPI backend. Open `/docs` for the API. Do not expose it publicly as-is.

## Run

```powershell
cd D:\AI-Agents\Backend-Development-Projects\fastapi-jobs-api
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

```powershell
python -m pytest -q
```
