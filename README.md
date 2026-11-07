# Backend Development Projects

Ten local **backend** APIs: five with **FastAPI** and five with **Django**. Each one is a JSON service with tests. No paid APIs.

Do not expose these apps publicly as-is.

## FastAPI

| # | Project | Backend task |
| --- | --- | --- |
| 1 | [fastapi-notes-api](fastapi-notes-api/) | CRUD notes |
| 2 | [fastapi-auth-api](fastapi-auth-api/) | JWT register, login, profile |
| 3 | [fastapi-orders-api](fastapi-orders-api/) | Orders and line items |
| 4 | [fastapi-files-api](fastapi-files-api/) | File upload and download |
| 5 | [fastapi-jobs-api](fastapi-jobs-api/) | Background jobs |

## Django

| # | Project | Backend task |
| --- | --- | --- |
| 6 | [django-blog-api](django-blog-api/) | Posts and comments |
| 7 | [django-bookstore-api](django-bookstore-api/) | Book search and pagination |
| 8 | [django-inventory-api](django-inventory-api/) | Stock and sales |
| 9 | [django-shortener-api](django-shortener-api/) | URL shortener |
| 10 | [django-issues-api](django-issues-api/) | Issue tracker |

## Quick start (FastAPI)

```powershell
cd D:\AI-Agents\Backend-Development-Projects\fastapi-notes-api
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

## Quick start (Django)

```powershell
cd D:\AI-Agents\Backend-Development-Projects\django-blog-api
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 127.0.0.1:8000
```
