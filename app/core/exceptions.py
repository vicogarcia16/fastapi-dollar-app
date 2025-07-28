class BanxicoAPIError(Exception):
    """Excepción para errores al interactuar con la API de Banxico."""
    def __init__(self, message: str = "Error al consultar la API de Banxico.", status_code: int = 500):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)

class ConfigError(Exception):
    """Excepción para errores de configuración."""
    def __init__(self, message: str = "Error de configuración.", status_code: int = 500):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)
