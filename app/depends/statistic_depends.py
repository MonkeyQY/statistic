from app.db import database
from app.repositories.statistic import StatisticRepository


def get_statistic_repository() -> StatisticRepository:
    return StatisticRepository(database)
