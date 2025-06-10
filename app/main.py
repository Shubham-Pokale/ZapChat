from fastapi import FastAPI
from .core.config import settings, logger
from .api.v1.api import api_router
from .core.middleware import log_requests


app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

app.include_router(api_router, prefix=settings.API_V1_STR)

# Add middleware
app.middleware("http")(log_requests)

logger.info("Application startup complete")