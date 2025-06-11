from fastapi import FastAPI, Request
from .core.config import settings, logger
from .api.v1.api import api_router
from .core.middleware import log_requests
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

app.include_router(api_router, prefix=settings.API_V1_STR)

# Add middleware
app.middleware("http")(log_requests)

logger.info("Application startup complete")

@app.get("/")
async def get_chat_page(request: Request):
    return templates.TemplateResponse("chat.html", {"request": request})