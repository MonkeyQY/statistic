import logging

from app.db.statistic import statistic
from app.db.db import database, engine, metadata

log = logging.getLogger("main.database")

# если таблицы не существуют, то создаем их
metadata.create_all(engine)
log.info("Create tables in database")
