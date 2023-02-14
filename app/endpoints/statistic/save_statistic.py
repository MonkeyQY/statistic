import logging
from datetime import datetime
from typing import Optional

from fastapi import APIRouter, Depends

from app import config
from app.depends.statistic_depends import get_statistic_repository
from app.models.statistic import SaveStatisticResponse, SaveStatistic, Statistic
from app.repositories.statistic import StatisticRepository

router = APIRouter()

log = logging.getLogger("save statistic")


@router.post(config.save_statistic_path)
async def save_statistic(
        saving_statistic: SaveStatistic,
        statistic_repository: StatisticRepository = Depends(get_statistic_repository),
) -> SaveStatisticResponse:
    log.info("Save statistic")
    statistic = prepare_statistic(saving_statistic)

    await statistic_repository.save_statistic(statistic)

    return SaveStatisticResponse(message="Statistic successfully saved")


def prepare_statistic(saving_statistic: SaveStatistic) -> Statistic:
    cpc, cpm = calculate_average_value(saving_statistic)

    statistic = Statistic(
        date=datetime(
            saving_statistic.date["year"],
            saving_statistic.date["month"],
            saving_statistic.date["day"],
        ),
        views=saving_statistic.views,
        clicks=saving_statistic.clicks,
        cost=saving_statistic.cost,
        cpc=cpc,
        cpm=cpm,
    )
    return statistic


def calculate_average_value(
        statistic: SaveStatistic,
) -> tuple[Optional[float], Optional[float]]:
    if statistic.clicks is None or statistic.cost is None or statistic.views is None:
        cpc = None
        cpm = None
        return cpc, cpm
    else:
        return calculate_average_amount_click(
            statistic.cost, statistic.clicks
        ), calculate_average_amount_1000_views(statistic.cost, statistic.views)


def calculate_average_amount_click(cost: float, clicks: int) -> float:
    return round(cost / clicks, 2)


def calculate_average_amount_1000_views(cost: float, views: int) -> float:
    return round(cost / views * 1000, 2)
