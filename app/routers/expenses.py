from typing import List

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Query,
    status,
)
from sqlalchemy.orm import Session

from app import crud, schemas
from app.auth import get_current_user
from app.database import get_db
from app.models import User

router = APIRouter(
    prefix="/expenses",
    tags=["Expenses"],
)


# ==========================
# Create Expense
# ==========================
@router.post(
    "/",
    response_model=schemas.ExpenseResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_expense(
    expense: schemas.ExpenseCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return crud.create_expense(
        db=db,
        expense=expense,
        user_id=current_user.id,
    )


# ==========================
# Get All Expenses
# ==========================
@router.get(
    "/",
    response_model=List[schemas.ExpenseResponse],
)
def get_expenses(
    search: str | None = Query(default=None),
    category: str | None = Query(default=None),
    payment_method: str | None = Query(default=None),
    sort: str = Query(default="desc"),
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=10, ge=1, le=100),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return crud.get_expenses(
        db=db,
        user_id=current_user.id,
        search=search,
        category=category,
        payment_method=payment_method,
        sort=sort,
        skip=skip,
        limit=limit,
    )


# ==========================
# Get Expense by ID
# ==========================
@router.get(
    "/{expense_id}",
    response_model=schemas.ExpenseResponse,
)
def get_expense(
    expense_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    expense = crud.get_expense_by_id(
        db=db,
        expense_id=expense_id,
        user_id=current_user.id,
    )

    if expense is None:
        raise HTTPException(
            status_code=404,
            detail="Expense not found",
        )

    return expense


# ==========================
# Update Expense
# ==========================
@router.put(
    "/{expense_id}",
    response_model=schemas.ExpenseResponse,
)
def update_expense(
    expense_id: int,
    expense: schemas.ExpenseUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    updated = crud.update_expense(
        db=db,
        expense_id=expense_id,
        expense=expense,
        user_id=current_user.id,
    )

    if updated is None:
        raise HTTPException(
            status_code=404,
            detail="Expense not found",
        )

    return updated


# ==========================
# Delete Expense
# ==========================
@router.delete(
    "/{expense_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_expense(
    expense_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    deleted = crud.delete_expense(
        db=db,
        expense_id=expense_id,
        user_id=current_user.id,
    )

    if deleted is None:
        raise HTTPException(
            status_code=404,
            detail="Expense not found",
        )

    return