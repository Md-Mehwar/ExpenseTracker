from sqlalchemy import asc, desc
from sqlalchemy.orm import Session

from app import models, schemas
from app.auth import hash_password


# ==========================
# USER CRUD
# ==========================

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        username=user.username,
        email=user.email,
        hashed_password=hash_password(user.password)
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


def get_user_by_email(db: Session, email: str):
    return (
        db.query(models.User)
        .filter(models.User.email == email)
        .first()
    )


# ==========================
# EXPENSE CRUD
# ==========================

def create_expense(
    db: Session,
    expense: schemas.ExpenseCreate,
    user_id: int
):
    db_expense = models.Expense(
        title=expense.title,
        amount=expense.amount,
        category=expense.category,
        description=expense.description,
        payment_method=expense.payment_method,
        user_id=user_id
    )

    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)

    return db_expense


def get_expenses(
    db: Session,
    user_id: int,
    search: str = None,
    category: str = None,
    payment_method: str = None,
    sort: str = "desc",
    skip: int = 0,
    limit: int = 10,
):
    query = db.query(models.Expense).filter(
        models.Expense.user_id == user_id
    )

    if search:
        query = query.filter(
            models.Expense.title.ilike(f"%{search}%")
        )

    if category:
        query = query.filter(
            models.Expense.category == category
        )

    if payment_method:
        query = query.filter(
            models.Expense.payment_method == payment_method
        )

    if sort.lower() == "asc":
        query = query.order_by(
            asc(models.Expense.created_at)
        )
    else:
        query = query.order_by(
            desc(models.Expense.created_at)
        )

    return query.offset(skip).limit(limit).all()


def get_expense_by_id(
    db: Session,
    expense_id: int,
    user_id: int
):
    return (
        db.query(models.Expense)
        .filter(
            models.Expense.id == expense_id,
            models.Expense.user_id == user_id
        )
        .first()
    )


def update_expense(
    db: Session,
    expense_id: int,
    expense: schemas.ExpenseUpdate,
    user_id: int
):
    db_expense = get_expense_by_id(
        db,
        expense_id,
        user_id
    )

    if db_expense is None:
        return None

    db_expense.title = expense.title
    db_expense.amount = expense.amount
    db_expense.category = expense.category
    db_expense.description = expense.description
    db_expense.payment_method = expense.payment_method

    db.commit()
    db.refresh(db_expense)

    return db_expense


def delete_expense(
    db: Session,
    expense_id: int,
    user_id: int
):
    db_expense = get_expense_by_id(
        db,
        expense_id,
        user_id
    )

    if db_expense is None:
        return None

    db.delete(db_expense)
    db.commit()

    return db_expense
from sqlalchemy import func
from app import models


def get_category_summary(db, user_id: int):
    return (
        db.query(
            models.Expense.category,
            func.sum(models.Expense.amount).label("total")
        )
        .filter(models.Expense.user_id == user_id)
        .group_by(models.Expense.category)
        .all()
    )