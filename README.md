# Expense Tracker Backend

A secure Expense Tracker REST API built with **FastAPI**, **PostgreSQL**, and **SQLAlchemy**.

## Features

- User Registration
- User Login using JWT Authentication
- Password Hashing
- Create Expense
- View Expenses
- Update Expense
- Delete Expense
- Search Expenses
- Filter by Category
- Filter by Payment Method
- Sorting
- Pagination
- Expense Analytics
  - Total Expenses
  - Category-wise Summary
  - Payment Method Summary
  - Monthly Summary
  - Top 5 Expenses

---

## Tech Stack

- FastAPI
- PostgreSQL
- SQLAlchemy
- Alembic
- Pydantic
- JWT Authentication
- Passlib (Password Hashing)
- Uvicorn

---

## Project Structure

```
ExpenseTracker
│
├── app
│   ├── routers
│   ├── auth.py
│   ├── crud.py
│   ├── database.py
│   ├── dependencies.py
│   ├── main.py
│   ├── models.py
│   └── schemas.py
│
├── alembic
├── requirements.txt
├── alembic.ini
└── README.md
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/Md-Mehwar/ExpenseTracker.git
```

Move into the project

```bash
cd ExpenseTracker
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

macOS/Linux

```bash
source .venv/bin/activate
```

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Configure your PostgreSQL database and update the `.env` file.

Run Alembic migrations

```bash
alembic upgrade head
```

Start the server

```bash
uvicorn app.main:app --reload
```

---

## API Documentation

Swagger UI

```
http://127.0.0.1:8000/docs
```

ReDoc

```
http://127.0.0.1:8000/redoc
```

---

## Future Improvements

- React Frontend
- Charts & Dashboard
- Budget Management
- Email Notifications
- CSV Export
- Receipt Upload
- Docker Support
- Deployment using Render/Vercel

---

## Author

**Mohammed Mehwar**
