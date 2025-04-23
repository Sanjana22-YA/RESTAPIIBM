from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY
from fastapi import HTTPException


def format_validation_errors(exc: RequestValidationError):
    formatted = {}
    for err in exc.errors():
        field = ".".join(str(loc) for loc in err["loc"] if loc!= "body")
        formatted[field] = f"{field.replace('_', ' ').capitalize()}: {err['msg']}"
    return formatted


def validation_exception_handler(request: Request, exec: RequestValidationError):
    return JSONResponse(
        status_code=HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "status": False,
            "message": "Validation Error",
            "errors": format_validation_errors(exec)
        }
    )

