from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

DATA_DIR = BASE_DIR / "data"
LOG_DIR = BASE_DIR / "logs"

EXPENSE_FILE = DATA_DIR / "expenses.json"

APP_NAME = "ExpenseFlow API"
APP_VERSION = "1.0.0"
