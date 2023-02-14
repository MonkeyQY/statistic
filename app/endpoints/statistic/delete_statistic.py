import logging

from fastapi import APIRouter, Depends

from app import config
from app.depends.statistic_depends import get_statistic_repository
from app.models.statistic import DeleteStatisticResponse
from app.repositories.statistic import StatisticRepository

router = APIRouter()

log = logging.getLogger("delete statistic")


@router.delete(config.delete_statistic_path)
async def delete_statistic(
    statistic_repository: StatisticRepository = Depends(get_statistic_repository),
) -> DeleteStatisticResponse:
    log.info("Delete statistic")

    await statistic_repository.delete_statistic()

    return DeleteStatisticResponse(message="Statistic successfully deleted")
