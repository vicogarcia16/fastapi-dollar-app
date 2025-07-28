from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from ..services.banxico_service import BanxicoService
from ..core.templates import templates
from ..schemas.dollar import DollarPrice, DollarPriceResponse
from ..core.exceptions import BanxicoAPIError, ConfigError

router = APIRouter(
    tags=["Dólar"],
    prefix="/banxico",
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_class=HTMLResponse)
async def get_dollar_price_html(request: Request, banxico_service: BanxicoService = Depends(BanxicoService)):
    context = {"request": request, "data": None, "error": None}
    try:
        dollar_price_data = banxico_service.get_dollar_price()
        context["data"] = dollar_price_data
    except (BanxicoAPIError, ConfigError) as e:
        context["error"] = e.message
    return templates.TemplateResponse("index.html", context)

@router.get("/data", response_model=DollarPriceResponse)
async def get_dollar_price_json(banxico_service: BanxicoService = Depends(BanxicoService)):
    dollar_price_data = banxico_service.get_dollar_price()
    if dollar_price_data:
        return DollarPriceResponse(data=DollarPrice(**dollar_price_data))
    raise BanxicoAPIError(message="No se pudo obtener el precio del dólar. Verifica el token de Banxico o la disponibilidad del servicio.", status_code=404)

