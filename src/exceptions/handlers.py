from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse


class ExpenseNotFoundError(Exception):
    pass


class ValidationError(Exception):
    pass


def register_exception_handlers(app: FastAPI):
    @app.exception_handler(ExpenseNotFoundError)
    async def expense_not_found_handler(request: Request, exc: ExpenseNotFoundError):
        return JSONResponse(
            status_code=404,
            content={
                "success": False,
                "message": str(exc),
            },
        )

    @app.exception_handler(ValidationError)
    async def validation_error_handler(request: Request, exc: ValidationError):
        return JSONResponse(
            status_code=400,
            content={
                "success": False,
                "message": str(exc),
            },
        )

    @app.exception_handler(Exception)
    async def generic_exception_handler(request: Request, exc: Exception):
        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "message": "Something went wrong.",
            },
        )
