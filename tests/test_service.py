from datetime import date

from src.models.expense import Expense
from src.repository.json_repository import JsonRepository
from src.schemas.expense_schema import ExpenseCreate
from src.services.expense_service import ExpenseService


def create_service(tmp_path):
    test_file = tmp_path / "expenses.json"
    repo = JsonRepository(test_file)
    return ExpenseService(repo)


def test_create_expense(tmp_path):
    service = create_service(tmp_path)
    expense = ExpenseCreate(
        title="Pizza",
        amount=450,
        category="Food",
        date=date(2026, 7, 31),
    )

    created = service.create_expense(expense)

    assert created.title == "Pizza"
    assert created.amount == 450
    assert created.category == "Food"


def test_get_total(tmp_path):
    service = create_service(tmp_path)
    service.repository.add(
        Expense(
            id="1",
            title="Pizza",
            amount=200,
            category="Food",
            date=date(2026, 7, 31),
        )
    )
    service.repository.add(
        Expense(
            id="2",
            title="Burger",
            amount=300,
            category="Food",
            date=date(2026, 7, 31),
        )
    )

    assert service.get_total() == 500


def test_filter_by_category(tmp_path):
    service = create_service(tmp_path)
    service.repository.add(
        Expense(
            id="1",
            title="Pizza",
            amount=200,
            category="Food",
            date=date(2026, 7, 31),
        )
    )
    service.repository.add(
        Expense(
            id="2",
            title="Uber",
            amount=150,
            category="Travel",
            date=date(2026, 7, 31),
        )
    )

    result = service.get_by_category("Food")

    assert len(result) == 1
    assert result[0].category == "Food"


def test_delete_expense(tmp_path):
    service = create_service(tmp_path)
    service.repository.add(
        Expense(
            id="1",
            title="Pizza",
            amount=200,
            category="Food",
            date=date(2026, 7, 31),
        )
    )

    service.delete_expense("1")

    assert len(service.get_all_expenses()) == 0
