from pydantic import BaseModel

class DollarPrice(BaseModel):
    fecha: str
    precio: float

class DollarPriceResponse(BaseModel):
    data: DollarPrice | None = None
    error: str | None = None
