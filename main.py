from fastapi import FastAPI
import logging
import asyncio
from utils import load_config
from constants import BASE_ROOT
from api import api_router
import uvicorn

from core.events import create_start_app_handler
logger = logging.getLogger("api")
logger.setLevel(logging.DEBUG)


def get_application() -> FastAPI:
    app = FastAPI()

    conf = load_config(BASE_ROOT / 'config' / 'config.yml')

    app.add_event_handler("startup", create_start_app_handler(app, conf))

    app.include_router(api_router)

    return app


app = get_application()
