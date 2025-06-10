from pydantic_settings import BaseSettings
from pydantic import field_validator, FieldValidationInfo
from pydantic.networks import PostgresDsn
from typing import Optional, Dict, Any
import logging


class Settings(BaseSettings):
    PROJECT_NAME : str = "FASTAPI APP"
    API_V1_STR: str = "/api/v1"
    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    PORT_NO : int = 5432
    DATABASE_URL: Optional[PostgresDsn] = None
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    APP_ENV: str = "dev"
    LOG_LEVEL: str = "INFO"
    LOG_FORMAT: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    

    @field_validator("DATABASE_URL", mode="before")
    @classmethod
    def assemble_db_connection(cls, v: Optional[str], info: FieldValidationInfo) -> Any:
        if isinstance(v, str):
            return v
        values = info.data
        return PostgresDsn.build(
            scheme="postgresql",
            username=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            path=values.get("POSTGRES_DB") or ""
        )

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()

# Configure root logger
logging.basicConfig(
    level=settings.LOG_LEVEL,
    format=settings.LOG_FORMAT,
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)