from datetime import datetime
from typing import Optional

from app.db.statistic import statistic
from app.models.statistic import Statistic
from app.repositories.base_respository import BaseRepository


class StatisticRepository(BaseRepository):
    async def save_statistic(self, save_statistic: Statistic) -> int:
        query = statistic.insert().values(
            date=save_statistic.date,
            views=save_statistic.views,
            clicks=save_statistic.clicks,
            cost=save_statistic.cost,
            cpc=save_statistic.cpc,
            cpm=save_statistic.cpm,
        )
        return await self.database.execute(query=query)

    async def get_statistic(
        self, date_from: datetime, date_to: datetime, sort_method: Optional[str]
    ) -> list[Statistic]:
        query = (
            statistic.select()
            .where(statistic.c.date >= date_from, statistic.c.date <= date_to)
            .order_by(sort_method)
        )
        result = await self.database.fetch_all(query=query)
        return [Statistic.parse_obj(item) for item in result]

    async def delete_statistic(self) -> None:
        query = statistic.delete()
        return await self.database.execute(query=query)
