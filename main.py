from fastapi import FastAPI
import logging
import asyncio
from api import api_router
import uvicorn

from core.events import create_start_app_handler
logger = logging.getLogger("api")
logger.setLevel(logging.DEBUG)


def get_application() -> FastAPI:
    app = FastAPI()

    app.add_event_handler("startup", create_start_app_handler(app))

    app.include_router(api_router)

    return app


app = get_application()
