import requests
import logging
from ..core.config import settings
from ..core.exceptions import BanxicoAPIError, ConfigError

logger = logging.getLogger(__name__)

class BanxicoService:
    def __init__(self):
        self.token = settings.BANXICO_TOKEN
        self.api_url = f"{settings.API_URL_BASE}/{settings.SERIE_DOLAR_FIX}/datos/oportuno"

    def get_dollar_price(self):
        if not self.token:
            logger.error("BANXICO_TOKEN no está configurado.")
            raise ConfigError(message="BANXICO_TOKEN no está configurado. Por favor, verifica tu archivo .env", status_code=500)

        headers = {"Bmx-Token": self.token}
        try:
            response = requests.get(self.api_url, headers=headers)
            response.raise_for_status()
            data = response.json()
            datos_serie = data.get("bmx", {}).get("series", [])
            if not datos_serie or not datos_serie[0].get("datos"):
                logger.warning("No se encontraron datos del tipo de cambio en la respuesta de la API de Banxico.")
                raise BanxicoAPIError(message="No se encontraron datos del tipo de cambio en la respuesta de la API de Banxico.", status_code=404)
            ultimo_dato = datos_serie[0]["datos"][0]
            return {
                "fecha": ultimo_dato["fecha"],
                "precio": float(ultimo_dato["dato"])
            }
        except requests.exceptions.RequestException as e:
            logger.error(f"Error al consultar la API de Banxico: {e}")
            raise BanxicoAPIError(message=f"Error de conexión con la API de Banxico: {e}", status_code=503)
        except (KeyError, IndexError, ValueError) as e:
            logger.error(f"Error al procesar los datos de la API de Banxico: {e}")
            raise BanxicoAPIError(message=f"Error al procesar los datos recibidos de Banxico: {e}", status_code=500)
