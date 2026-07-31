from fastapi import APIRouter, Query

from src.schemas.expense_schema import ExpenseCreate, ExpenseResponse
from src.services.expense_service import ExpenseService

router = APIRouter(
    prefix="/expenses",
    tags=["Expenses"],
)
service = ExpenseService()


@router.post("", response_model=ExpenseResponse, status_code=201)
def create_expense(expense: ExpenseCreate):
    return service.create_expense(expense)


@router.get("", response_model=list[ExpenseResponse])
def get_expenses(category: str | None = Query(default=None)):
    if category:
        return service.get_by_category(category)
    return service.get_all_expenses()


@router.get("/total")
def get_total(category: str | None = Query(default=None)):
    total = service.get_total(category)
    return {"total": total}


@router.delete("/{expense_id}", status_code=200)
def delete_expense(expense_id: str):
    service.delete_expense(expense_id)
    return {"message": "Expense deleted successfully."}
