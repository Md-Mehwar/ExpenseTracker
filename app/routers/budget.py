from typing import List

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)
from sqlalchemy.orm import Session

from app import crud, schemas
from app.auth import get_current_user
from app.database import get_db
from app.models import User

router = APIRouter(
    prefix="/budgets",
    tags=["Budgets"],
)


# ==========================
# Create / Update Budget
# ==========================
@router.post(
    "/",
    response_model=schemas.BudgetResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_budget(
    budget: schemas.BudgetCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return crud.create_budget(
        db=db,
        budget=budget,
        user_id=current_user.id,
    )


# ==========================
# Get All Budgets
# ==========================
@router.get(
    "/",
    response_model=List[schemas.BudgetResponse],
)
def get_budgets(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return crud.get_all_budgets(
        db=db,
        user_id=current_user.id,
    )


# ==========================
# Get Budget by Month
# ==========================
@router.get(
    "/{month}",
    response_model=schemas.BudgetResponse,
)
def get_budget(
    month: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    budget = crud.get_budget(
        db=db,
        month=month,
        user_id=current_user.id,
    )

    if budget is None:
        raise HTTPException(
            status_code=404,
            detail="Budget not found",
        )

    return budget


# ==========================
# Delete Budget
# ==========================
@router.delete(
    "/{budget_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_budget(
    budget_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    deleted = crud.delete_budget(
        db=db,
        budget_id=budget_id,
        user_id=current_user.id,
    )

    if deleted is None:
        raise HTTPException(
            status_code=404,
            detail="Budget not found",
        )

    return