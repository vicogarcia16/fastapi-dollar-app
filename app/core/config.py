from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    BANXICO_TOKEN: str
    SERIE_DOLAR_FIX: str = "SF43718"
    API_URL_BASE: str = "https://www.banxico.org.mx/SieAPIRest/service/v1/series"
    API_VERSION: str = "1"

settings = Settings()
