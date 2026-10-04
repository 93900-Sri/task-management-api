Task Management API

A RESTful Task Management API built with FastAPI and PostgreSQL, featuring JWT-based authentication, password hashing, task CRUD operations, pagination, and database migrations.

Features

Authentication

- User registration
- User login
- Password hashing using bcrypt
- JWT access-token authentication
- Protected API endpoints

Task Management

- Create tasks
- Retrieve tasks
- Retrieve a task by ID
- Update tasks using "PUT"
- Partially update tasks using "PATCH"
- Delete tasks
- Mark tasks as completed
- User-specific task access

API Features

- Request validation using Pydantic
- Pagination
- API error handling
- HTTP status codes
- Swagger/OpenAPI documentation

Database

- PostgreSQL
- SQLAlchemy ORM
- Alembic database migrations

Development

- Docker Compose for the PostgreSQL environment
- Environment variables for configuration
- Git/GitHub version control

Tech Stack

Technology| Purpose
Python| Backend programming
FastAPI| REST API framework
PostgreSQL| Relational database
SQLAlchemy| ORM and database interaction
Pydantic| Request/response validation
bcrypt| Password hashing
JWT| Authentication
Alembic| Database migrations
Docker Compose| PostgreSQL environment
Insomnia
Swagger / OpenAPI| API documentation

API Endpoints

Authentication

Method| Endpoint| Description
"POST"| "/auth/register"| Register a new user
"POST"| "/auth/login"| Login and obtain JWT token

Tasks

Method| Endpoint| Description
"POST"| "/tasks"| Create a task
"GET"| "/tasks"| Get tasks
"GET"| "/tasks/{task_id}"| Get a task by ID
"PUT"| "/tasks/{task_id}"| Replace/update a task
"PATCH"| "/tasks/{task_id}"| Partially update a task
"DELETE"| "/tasks/{task_id}"| Delete a task

«Endpoint paths should be kept consistent with the routes currently defined in the application.»

Project Structure

task-management-api/
│
├── alembic/
├── migrations/
├── routers/
│   ├── auth.py
│   ├── tasks.py
│   └── users.py
│
├── .env.example
├── .gitignore
├── alembic.ini
├── crud.py
├── database.py
├── docker-compose.yml
├── main.py
├── models.py
├── requirements.txt
├── schemas.py
├── security.py
└── README.md

How to Run Locally

1. Clone the repository

git clone <repository-url>
cd task-management-api

2. Create a virtual environment

python -m venv venv

3. Activate the virtual environment

Windows:

venv\Scripts\activate

macOS / Linux:

source venv/bin/activate

4. Install dependencies

pip install -r requirements.txt

5. Configure environment variables

Create a ".env" file using ".env.example" as the template.

Add your local database configuration and JWT-related secrets.

Never commit ".env" to GitHub.

6. Start PostgreSQL

If using Docker Compose:

docker compose up -d

7. Run database migrations

alembic upgrade head

8. Start the FastAPI server

uvicorn main:app --reload

The API will be available at:

http://127.0.0.1:8000

Swagger UI:

http://127.0.0.1:8000/docs

Authentication Flow

Register
   ↓
Password Hashing (bcrypt)
   ↓
Login
   ↓
JWT Token
   ↓
Authorization Header
   ↓
Protected Task Endpoints

For protected endpoints, provide the JWT access token in the authorization header:

Authorization: Bearer <access_token>

Database Migrations

Create a new migration:

alembic revision --autogenerate -m "describe change"

Apply migrations:

alembic upgrade head

Security

- Passwords are hashed using bcrypt before being stored.
- JWT tokens are used to protect authenticated endpoints.
- Sensitive configuration is stored in environment variables.
- ".env" is excluded from Git version control.
- ".env.example" is provided as a configuration template.

API Documentation

FastAPI automatically provides interactive API documentation through Swagger UI:

http://127.0.0.1:8000/docs

The OpenAPI documentation can also be accessed at:

http://127.0.0.1:8000/openapi.json

Project Highlights

This project demonstrates practical backend development using:

- REST API development with FastAPI
- Authentication and authorization
- JWT-based security
- bcrypt password hashing
- PostgreSQL database integration
- SQLAlchemy ORM
- CRUD operations
- Pydantic validation
- Pagination
- Database migrations with Alembic
- Docker-based database setup
- Swagger/OpenAPI documentation

Future Improvements

Possible future improvements include:

- Automated test coverage
- Role-based authorization
- Refresh tokens
- Rate limiting
- CI/CD pipeline
- Production deployment
