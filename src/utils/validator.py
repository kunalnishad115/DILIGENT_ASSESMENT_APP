from fastapi import HTTPException
from src.schemas.expense_schema import ExpenseCreate


class ExpenseValidator:
    @staticmethod
    def validate(expense: ExpenseCreate) -> None:
        title = expense.title.strip()
        category = expense.category.strip()
        if not title:
            raise HTTPException(
                status_code=400,
                detail="Title cannot be empty."
            )
        if not category:
            raise HTTPException(
                status_code=400,
                detail="Category cannot be empty."
            )