from typing import Optional
from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


# =========================
# USER SCHEMAS
# =========================

class UserCreate(BaseModel):
    username: str
    email: str
    password: str


class UserLogin(BaseModel):
    email: str
    password: str


class UserResponse(BaseModel):
    id: int
    username: str
    email: str

    model_config = ConfigDict(from_attributes=True)


# =========================
# EXPENSE SCHEMAS
# =========================

class ExpenseBase(BaseModel):
    title: str = Field(..., min_length=2, max_length=100)
    amount: float = Field(..., gt=0)
    category: str
    description: Optional[str] = None
    payment_method: str


class ExpenseCreate(ExpenseBase):
    pass


class ExpenseUpdate(ExpenseBase):
    pass


class ExpenseResponse(ExpenseBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


# =========================
# ANALYTICS SCHEMAS
# =========================

class CategorySummary(BaseModel):
    category: str
    total: float

    model_config = ConfigDict(from_attributes=True)


# =========================
# BUDGET SCHEMAS
# =========================

class BudgetBase(BaseModel):
    month: str = Field(..., examples=["2026-10"])
    amount: float = Field(..., gt=0)


class BudgetCreate(BudgetBase):
    pass


class BudgetUpdate(BudgetBase):
    pass


class BudgetResponse(BudgetBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
class ExpensePagination(BaseModel):
    items: list[ExpenseResponse]
    total: int

    model_config = ConfigDict(from_attributes=True)