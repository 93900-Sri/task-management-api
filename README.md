# Task Management API

A practical beginner-friendly REST API using FastAPI, PostgreSQL, SQLAlchemy, Pydantic, JWT, Argon2, Alembic and Pytest.

## Architecture

Client/Swagger -> Router -> Service -> Repository -> SQLAlchemy -> PostgreSQL

## Features

- User registration and login
- Argon2 password hashing
- JWT authentication
- Current user profile
- Task CRUD
- PUT and PATCH
- Mark task complete
- Task ownership
- Pagination, filtering and sorting
- Validation
- Alembic migrations
- Tests

## Run locally

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

Copy `.env.example` to `.env`, then:

```bash
docker compose up -d
alembic upgrade head
uvicorn main:app --reload
```

Open http://127.0.0.1:8000/docs

## Endpoints

POST /users/register
POST /users/login
GET /users/me

POST /tasks
GET /tasks
GET /tasks/{task_id}
PUT /tasks/{task_id}
PATCH /tasks/{task_id}
PATCH /tasks/{task_id}/complete
DELETE /tasks/{task_id}

## Tests

```bash
pytest
```

Never commit `.env` or passwords/secrets to GitHub.
