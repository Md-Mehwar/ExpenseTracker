from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func, desc

from app.database import get_db
from app.auth import get_current_user
from app.models import Expense, User

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)


@router.get("/summary")
def summary(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    total_expenses = (
        db.query(Expense)
        .filter(Expense.user_id == current_user.id)
        .count()
    )

    total_amount = (
        db.query(func.sum(Expense.amount))
        .filter(Expense.user_id == current_user.id)
        .scalar()
        or 0
    )

    average_expense = (
        db.query(func.avg(Expense.amount))
        .filter(Expense.user_id == current_user.id)
        .scalar()
        or 0
    )

    highest_expense = (
        db.query(func.max(Expense.amount))
        .filter(Expense.user_id == current_user.id)
        .scalar()
        or 0
    )

    lowest_expense = (
        db.query(func.min(Expense.amount))
        .filter(Expense.user_id == current_user.id)
        .scalar()
        or 0
    )

    return {
        "total_expenses": total_expenses,
        "total_amount": round(total_amount, 2),
        "average_expense": round(average_expense, 2),
        "highest_expense": round(highest_expense, 2),
        "lowest_expense": round(lowest_expense, 2)
    }


@router.get("/category-summary")
def category_summary(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    results = (
        db.query(
            Expense.category,
            func.sum(Expense.amount).label("total")
        )
        .filter(Expense.user_id == current_user.id)
        .group_by(Expense.category)
        .all()
    )

    return [
        {
            "category": category,
            "total": round(total, 2)
        }
        for category, total in results
    ]


@router.get("/payment-method")
def payment_method_summary(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    results = (
        db.query(
            Expense.payment_method,
            func.sum(Expense.amount).label("total")
        )
        .filter(Expense.user_id == current_user.id)
        .group_by(Expense.payment_method)
        .all()
    )

    return [
        {
            "payment_method": payment,
            "total": round(total, 2)
        }
        for payment, total in results
    ]


@router.get("/monthly")
def monthly_summary(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    results = (
        db.query(
            func.strftime("%Y-%m", Expense.created_at).label("month"),
            func.sum(Expense.amount).label("total")
        )
        .filter(Expense.user_id == current_user.id)
        .group_by("month")
        .order_by("month")
        .all()
    )

    return [
        {
            "month": month,
            "total": round(total, 2)
        }
        for month, total in results
    ]


@router.get("/top-expenses")
def top_expenses(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    expenses = (
        db.query(Expense)
        .filter(Expense.user_id == current_user.id)
        .order_by(desc(Expense.amount))
        .limit(5)
        .all()
    )

    return expenses

