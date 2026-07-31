import json
from dataclasses import asdict
from pathlib import Path
from src.config.settings import DATA_DIR, EXPENSE_FILE
from src.models.expense import Expense


class JsonRepository:
    def __init__(self):
        DATA_DIR.mkdir(exist_ok=True)
        if not EXPENSE_FILE.exists():
            EXPENSE_FILE.write_text("[]")

    def _read(self) -> list[Expense]:
        with open(EXPENSE_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
        return [Expense(**item) for item in data]

    def _write(self, expenses: list[Expense]) -> None:
        with open(EXPENSE_FILE, "w", encoding="utf-8") as file:
            json.dump(
                [asdict(expense) for expense in expenses],
                file,
                indent=4,
                default=str,
            )

    def get_all(self) -> list[Expense]:
        return self._read()

    def add(self, expense: Expense) -> Expense:
        expenses = self._read()
        expenses.append(expense)
        self._write(expenses)
        return expense

    def delete(self, expense_id: str) -> bool:
        expenses = self._read()
        updated = [e for e in expenses if e.id != expense_id]

        if len(updated) == len(expenses):
            return False

        self._write(updated)
        return True