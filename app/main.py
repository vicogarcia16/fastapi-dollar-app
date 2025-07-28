from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from .routers import dollar_price
from .core.config import settings
from .core.templates import templates
from .core.exception_handlers import register_exception_handlers

app = FastAPI(
    title="API de Precio del Dólar en México",
    description="Una API simple para obtener el tipo de cambio del dólar (FIX) en México, utilizando datos del Banco de México.",
    version=f"{settings.API_VERSION}.0.0",
    docs_url="/documentation",
    redoc_url=None,
)

register_exception_handlers(app)
app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.include_router(dollar_price.router, prefix=f"/api/v{settings.API_VERSION}")

@app.get("/", tags=["Bienvenida"], response_class=HTMLResponse)
async def welcome(request: Request):
    return templates.TemplateResponse("welcome.html", {"request": request})
