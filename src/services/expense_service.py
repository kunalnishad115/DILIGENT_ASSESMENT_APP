from uuid import uuid4

from src.exceptions.handlers import ExpenseNotFoundError
from src.models.expense import Expense
from src.repository.json_repository import JsonRepository
from src.schemas.expense_schema import ExpenseCreate
from src.utils.logger import get_logger
from src.utils.validator import ExpenseValidator


class ExpenseService:
    def __init__(self, repository=None):
        self.repository = repository or JsonRepository()
        self.logger = get_logger(__name__)

    def create_expense(self, expense: ExpenseCreate) -> Expense:
        """Create and save a new expense."""
        ExpenseValidator.validate(expense)
        new_expense = Expense(
            id=str(uuid4()),
            title=expense.title.strip(),
            amount=expense.amount,
            category=expense.category.strip().title(),
            date=expense.date,
        )

        saved_expense = self.repository.add(new_expense)
        self.logger.info(
            f"Created expense '{saved_expense.title}' ({saved_expense.id})"
        )
        return saved_expense

    def get_all_expenses(self) -> list[Expense]:
        """Return all expenses."""
        expenses = self.repository.get_all()
        self.logger.info(f"Fetched {len(expenses)} expense(s)")
        return expenses

    def get_by_category(self, category: str) -> list[Expense]:
        """Return expenses for a specific category."""
        expenses = self.repository.get_all()
        category = category.strip().lower()
        filtered = [
            expense for expense in expenses if expense.category.lower() == category
        ]

        self.logger.info(
            f"Fetched {len(filtered)} expense(s) for category '{category}'"
        )
        return filtered

    def get_total(self, category: str | None = None) -> float:
        """Calculate total expenses."""
        expenses = self.repository.get_all()

        if category:
            category = category.strip().lower()
            expenses = [
                expense for expense in expenses if expense.category.lower() == category
            ]

        total = round(sum(exp.amount for exp in expenses), 2)

        if category:
            self.logger.info(f"Calculated total for '{category}': {total}")
        else:
            self.logger.info(f"Calculated overall total: {total}")

        return total

    def delete_expense(self, expense_id: str) -> None:
        """Delete an expense by ID."""
        deleted = self.repository.delete(expense_id)
        if not deleted:
            raise ExpenseNotFoundError("Expense not found.")

        self.logger.info(f"Deleted expense: {expense_id}")
