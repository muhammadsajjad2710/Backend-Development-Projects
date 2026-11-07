# Django Issues API

JSON issue tracker.

Local Django JSON API with SQLite. Do not expose it publicly as-is.

## Run

```powershell
cd D:\AI-Agents\Backend-Development-Projects\django-issues-api
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 127.0.0.1:8000
```

```powershell
python manage.py test
```
