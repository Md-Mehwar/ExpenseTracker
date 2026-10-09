# Expense Tracker Backend

A REST API built using FastAPI and PostgreSQL.

## Features
- JWT Authentication
- User Registration/Login
- CRUD Expenses
- Search
- Filtering
- Sorting
- Pagination
- Expense Analytics
- PostgreSQL
- Alembic Migrations

## Tech Stack
- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- Pydantic
- JWT
- Passlib
- Uvicorn

## Installation

git clone ...
cd ExpenseTracker

pip install -r requirements.txt

uvicorn app.main:app --reload

## API Documentation

http://127.0.0.1:8000/docs

## Project Structure

app/
routers/
models.py
schemas.py
crud.py
...
