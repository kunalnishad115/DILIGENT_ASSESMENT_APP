from dataclasses import dataclass
from datetime import date


@dataclass
class Expense:
    id: str
    title: str
    amount: float
    category: str
    date: date
