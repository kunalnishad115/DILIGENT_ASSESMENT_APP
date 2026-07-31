from fastapi.testclient import TestClient

from src.main import app
from src.repository.json_repository import JsonRepository

client = TestClient(app)


def reset_data():
    repo = JsonRepository()
    repo._write([])


def test_create_expense():
    reset_data()

    response = client.post(
        "/expenses",
        json={
            "title": "Pizza",
            "amount": 450,
            "category": "Food",
            "date": "2026-07-31",
        },
    )

    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Pizza"
    assert data["amount"] == 450
    assert data["category"] == "Food"


def test_get_all_expenses():
    reset_data()

    client.post(
        "/expenses",
        json={
            "title": "Pizza",
            "amount": 450,
            "category": "Food",
            "date": "2026-07-31",
        },
    )

    response = client.get("/expenses")
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_filter_by_category():
    reset_data()

    client.post(
        "/expenses",
        json={
            "title": "Pizza",
            "amount": 450,
            "category": "Food",
            "date": "2026-07-31",
        },
    )
    client.post(
        "/expenses",
        json={
            "title": "Cab",
            "amount": 200,
            "category": "Travel",
            "date": "2026-07-31",
        },
    )

    response = client.get("/expenses?category=Food")
    assert response.status_code == 200

    data = response.json()
    assert len(data) == 1
    assert data[0]["category"] == "Food"


def test_get_total():
    reset_data()

    client.post(
        "/expenses",
        json={
            "title": "Pizza",
            "amount": 400,
            "category": "Food",
            "date": "2026-07-31",
        },
    )
    client.post(
        "/expenses",
        json={
            "title": "Burger",
            "amount": 600,
            "category": "Food",
            "date": "2026-07-31",
        },
    )

    response = client.get("/expenses/total")
    assert response.status_code == 200
    assert response.json()["total"] == 1000


def test_delete_expense():
    reset_data()

    response = client.post(
        "/expenses",
        json={
            "title": "Pizza",
            "amount": 450,
            "category": "Food",
            "date": "2026-07-31",
        },
    )

    expense_id = response.json()["id"]
    delete_response = client.delete(f"/expenses/{expense_id}")
    assert delete_response.status_code == 200

    expenses = client.get("/expenses").json()
    assert len(expenses) == 0


def test_delete_invalid_expense():
    reset_data()

    response = client.delete("/expenses/invalid-id")
    assert response.status_code == 404
