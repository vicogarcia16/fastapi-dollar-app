from fastapi import Request, HTTPException, status, FastAPI
from fastapi.responses import JSONResponse
from .exceptions import BanxicoAPIError, ConfigError

async def banxico_api_exception_handler(request: Request, exc: BanxicoAPIError):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "detail": exc.message,
            "code": "BANXICO_API_ERROR"
        },
    )

async def config_exception_handler(request: Request, exc: ConfigError):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "detail": exc.message,
            "code": "CONFIG_ERROR"
        },
    )

async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "message": exc.detail or "HTTP error"
        }
    )

async def general_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "message": "Internal Server Error"
        }
    )

def register_exception_handlers(app: FastAPI):
    app.add_exception_handler(BanxicoAPIError, banxico_api_exception_handler)
    app.add_exception_handler(ConfigError, config_exception_handler)
    app.add_exception_handler(HTTPException, http_exception_handler)
    app.add_exception_handler(Exception, general_exception_handler)
