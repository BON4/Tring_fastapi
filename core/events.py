from typing import Callable
from fastapi import FastAPI
from utils import setup_executor


def create_start_app_handler(app: FastAPI, conf: dict) -> Callable:  # type: ignore
    async def start_app() -> None:
        executor = await setup_executor(conf)

    return start_app
