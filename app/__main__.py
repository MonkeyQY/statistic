import logging
from logging import Logger

import uvicorn

from fastapi import FastAPI

from app.endpoints.statistic.save_statistic import router as save_statistic_router
from app.endpoints.statistic.delete_statistic import router as delete_statistic_router
from app.endpoints.statistic.get_statistic import router as get_statistic_router

import config
from app.db import database

host = config.host
port = config.port

app = FastAPI(
    title="Listener",
    description="API for the application",
    version="1.0.0",
    docs_url=config.docs_url,
)

app.include_router(
    save_statistic_router,
    prefix=config.prefix_api,
    tags=["Statistic"],
)

app.include_router(
    delete_statistic_router,
    prefix=config.prefix_api,
    tags=["Statistic"],
)

app.include_router(
    get_statistic_router,
    prefix=config.prefix_api,
    tags=["Statistic"],
)

if config.use_log_file:
    logging.basicConfig(
        filename="logs.log",
        format="{asctime} : {levelname} : {name} : {message}",
        style="{",
        level=logging.DEBUG,
    )
else:
    logging.basicConfig(
        format="{asctime} : {levelname} : {name} : {message}",
        style="{",
        level=logging.INFO,
    )

log: Logger = logging.getLogger("main")


@app.on_event("startup")
async def startup_event() -> None:
    await database.connect()
    log.info("Database connected")


@app.on_event("shutdown")
async def shutdown_event() -> None:
    await database.connect()
    log.info("Database disconnected")


if __name__ == "__main__":
    uvicorn.run(
        "__main__:app", host=host, port=port, reload=config.reload, log_config=None
    )
