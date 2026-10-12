# 💰 Expense Tracker

A modern Full Stack Expense Tracker built using **React**, **FastAPI**, and **SQLite/PostgreSQL**. The application allows users to securely manage their expenses with authentication, budgeting, analytics, and export features.

---

## 🚀 Features

### Authentication
- User Registration
- User Login
- JWT Authentication
- Protected Routes
- Logout

### Expense Management
- Add Expense
- Edit Expense
- Delete Expense
- Search Expenses
- Category Filter
- Sort Expenses
- Pagination

### Budget
- Set Monthly Budget
- Remaining Budget Calculation

### Analytics
- Category-wise Expense Analysis
- Total Expense Summary

### Export
- Export Expenses to CSV
- Export Expenses to PDF

### UI
- Responsive Design
- Material UI
- Dark Mode
- Toast Notifications
- Loading Indicators

---

# 🛠 Tech Stack

## Frontend

- React
- Material UI
- Axios
- React Router
- React Toastify

## Backend

- FastAPI
- SQLAlchemy
- Alembic
- JWT Authentication
- Passlib
- Pydantic

## Database

- SQLite (Development)
- PostgreSQL (Production Ready)

---

# 📂 Project Structure

```
ExpenseTracker
│
├── backend
│   ├── app
│   ├── alembic
│   ├── requirements.txt
│   └── main.py
│
├── frontend
│   ├── src
│   ├── public
│   ├── package.json
│   └── vite.config.js
│
└── README.md
```

---

# ⚙️ Installation

## Backend

```bash
cd backend

python -m venv .venv

source .venv/bin/activate      # Mac/Linux

pip install -r requirements.txt

uvicorn app.main:app --reload
```

Backend runs on

```
http://127.0.0.1:8000
```

Swagger

```
http://127.0.0.1:8000/docs
```

---

## Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend runs on

```
http://localhost:5173
```

---

# 📸 Screenshots

Add screenshots here after deployment.

- Login Page
- Register Page
- Dashboard
- Expense List
- Analytics
- Budget
- Dark Mode
- PDF Export

---

# 🔐 Authentication

JWT-based authentication is used.

Each user can only access their own expenses.

---

# 📄 API Endpoints

## Authentication

- POST /register
- POST /login

## Expenses

- GET /expenses
- POST /expenses
- PUT /expenses/{id}
- DELETE /expenses/{id}

## Budget

- GET /budget
- POST /budget

## Analytics

- GET /analytics

---

# 🌟 Future Improvements

- Date Range Filter
- Expense Categories Management
- Monthly Reports
- Email Notifications
- Multi-Currency Support

---

# 👨‍💻 Author

**Mohammed Mehwar**

B.E. Electronics & Communication Engineering

BMS College of Engineering
