from fastapi import FastAPI

from src.api.expense_routes import router as expense_router
from src.config.settings import APP_NAME, APP_VERSION
from src.exceptions.handlers import register_exception_handlers

app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
    description="REST API for managing personal expenses.",
)
register_exception_handlers(app)
app.include_router(expense_router)


@app.get("/")
def home():
    return {"message": "ExpenseFlow API is running"}


@app.get("/health")
def health():
    return {"status": "healthy"}
