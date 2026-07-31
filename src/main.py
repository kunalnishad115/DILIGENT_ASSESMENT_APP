from fastapi import FastAPI

from src.api.expense_routes import router as expense_router
from src.config.settings import APP_NAME, APP_VERSION

app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
    description="REST API for managing personal expenses.",
)

app.include_router(expense_router)


@app.get("/")
def home():
    return {"message": "ExpenseFlow API is running"}


@app.get("/health")
def health():
    return {"status": "healthy"}