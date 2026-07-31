from uuid import uuid4
from src.models.expense import Expense
from src.repository.json_repository import JsonRepository
from src.schemas.expense_schema import ExpenseCreate
from src.utils.logger import get_logger
from src.utils.validator import ExpenseValidator


class ExpenseService:
    def __init__(self):
        self.repository = JsonRepository()
        self.logger = get_logger(__name__)

    def create_expense(self, expense: ExpenseCreate) -> Expense:
        ExpenseValidator.validate(expense)
        new_expense = Expense(
            id=str(uuid4()),
            title=expense.title.strip(),
            amount=expense.amount,
            category=expense.category.strip().title(),
            date=expense.date,
        )

        self.repository.add(new_expense)
        self.logger.info(f"Expense created: {new_expense.id}")
        return new_expense

    def get_all_expenses(self) -> list[Expense]:
        return self.repository.get_all()



    def get_by_category(self, category: str) -> list[Expense]:
        expenses = self.repository.get_all()
        category = category.strip().lower()

        return [
            expense for expense in expenses
            if expense.category.lower() == category
        ]

    def get_total(self, category: str | None = None) -> float:
        expenses = self.repository.get_all()

        if category:
            category = category.strip().lower()
            expenses = [
                expense for expense in expenses
                if expense.category.lower() == category
            ]

        return round(sum(exp.amount for exp in expenses), 2)

    def delete_expense(self, expense_id: str) -> bool:
        deleted = self.repository.delete(expense_id)
        if deleted:
            self.logger.info(f"Expense deleted: {expense_id}")

        return deleted