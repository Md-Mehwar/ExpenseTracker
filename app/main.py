from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import engine
from app import models
from app.routers import expenses, users, analytics

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Expense Tracker API"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/")
def root():
    return {
        "message": "Expense Tracker API is running!"
    }
app.include_router(users.router)
app.include_router(expenses.router)
app.include_router(analytics.router)