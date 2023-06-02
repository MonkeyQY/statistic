import logging
from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException

from app import config
from app.depends.statistic_depends import get_statistic_repository
from app.models.statistic import GetStatisticResponse, GetStatistic
from app.repositories.statistic import StatisticRepository

router = APIRouter()

log = logging.getLogger("get statistic")


@router.post(config.get_statistic_path)
async def get_statistic(
    date: GetStatistic,
    statistic_repository: StatisticRepository = Depends(get_statistic_repository),
) -> GetStatisticResponse:
    log.info("Get statistic")
    date_from = datetime(
        date.date_from["year"], date.date_from["month"], date.date_from["day"]
    )
    date_to = datetime(date.date_to["year"], date.date_to["month"], date.date_to["day"])

    try:
        list_statistic = await statistic_repository.get_statistic(
            date_from, date_to, date.sort_method
        )
    except Exception:
        raise HTTPException(status_code=400, detail="Wrong sort method")

    log.info("Get statistic success")
    return GetStatisticResponse(statistics=list_statistic)
