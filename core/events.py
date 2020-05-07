from typing import Callable
from fastapi import FastAPI
from utils import setup_executor
from hendlers import SiteHandler
from utils import load_config
from constants import BASE_ROOT
import asyncio


def create_start_app_handler(app: FastAPI) -> Callable:  # type: ignore
    async def start_app() -> None:
        conf = load_config(BASE_ROOT / 'config' / 'config.yml')
        executor = await setup_executor(conf)
        handler = SiteHandler(conf, executor, BASE_ROOT)

    return start_app
