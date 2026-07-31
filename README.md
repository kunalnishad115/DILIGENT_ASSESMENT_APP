
# ExpenseFlow API

ExpenseFlow API is a simple REST API built with FastAPI to manage personal expenses. It allows users to add, view, filter, calculate, and delete expenses. Data is stored in a local JSON file, so no database setup is required.

---

## Features

* Add a new expense
* View all expenses
* Filter expenses by category
* Calculate total expenses
* Calculate total expenses for a specific category
* Delete an expense
* Input validation using Pydantic
* Unit tests and API tests with Pytest

---

## Project Structure

```
expenseflow-api/

├── README.md
├── AI_NOTES.md
├── requirements.txt
├── data/
│   └── expenses.json
├── src/
│   ├── api/
│   ├── config/
│   ├── exceptions/
│   ├── models/
│   ├── repository/
│   ├── schemas/
│   ├── services/
│   ├── utils/
│   └── main.py
└── tests/
    ├── test_api.py
    └── test_service.py
```

---

## Installation

Clone the repository.

```bash
git clone <repository-url>
cd expenseflow-api
```

Create a virtual environment using uv.

```bash
uv venv
```

Activate the environment.

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies.

```bash
uv pip install -r requirements.txt
```

---

## Run the Server

```bash
uv run uvicorn src.main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

---

## Run Tests

Run all tests:

```bash
uv run pytest
```

Run tests with coverage:

```bash
uv run pytest --cov=src
```

---

## API Endpoints

| Method | Endpoint                          | Description           |
| ------ | --------------------------------- | --------------------- |
| POST   | `/expenses`                     | Create a new expense  |
| GET    | `/expenses`                     | Get all expenses      |
| GET    | `/expenses?category=Food`       | Filter by category    |
| GET    | `/expenses/total`               | Get total expenses    |
| GET    | `/expenses/total?category=Food` | Get total by category |
| DELETE | `/expenses/{expense_id}`        | Delete an expense     |

---

## Sample Request

### Create Expense

```json
{
  "title": "Pizza",
  "amount": 450,
  "category": "Food",
  "date": "2026-07-31"
}
```

---

## Tech Stack

* Python 3.11
* FastAPI
* Uvicorn
* Pydantic
* Pytest

---

## Testing

The project includes both service-level and API-level tests.

Current test status:

* 10 tests passing
* 95% code coverage

---

## Notes

This project uses a local JSON file for persistence instead of a database to keep the implementation simple, as required in the assignment.
