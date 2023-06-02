from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from app.db.sort_methods import SortMethods


class Statistic(BaseModel):
    date: datetime
    views: Optional[int]
    clicks: Optional[int]
    cost: Optional[float]
    cpc: Optional[float]
    cpm: Optional[float]


class Statistics(BaseModel):
    statistics: list[Statistic]


class SaveStatistic(BaseModel):
    date: dict
    views: Optional[int]
    clicks: Optional[int]
    cost: Optional[float]

    class Config:
        schema_extra = {
            "example": {
                "date": {"year": 2021, "month": 1, "day": 1},
                "views": 100,
                "clicks": 10,
                "cost": 10.0,
            }
        }


class SaveStatisticResponse(BaseModel):
    message: str


class GetStatistic(BaseModel):
    date_from: dict
    date_to: dict
    sort_method: Optional[SortMethods]

    class Config:
        schema_extra = {
            "example": {
                "date_from": {"year": 2021, "month": 1, "day": 1},
                "date_to": {"year": 2021, "month": 1, "day": 1},
                "sort_method": SortMethods.views,
            }
        }


class GetStatisticResponse(BaseModel):
    statistics: Statistics

    class Config:
        schema_extra = {
            "example": {
                "statistics": [
                    {
                        "date": "2021-01-01T00:00:00",
                        "views": 100,
                        "clicks": 10,
                        "cost": 10.0,
                        "cpc": 1.0,
                        "cpm": 100.0,
                    }
                ]
            }
        }


class DeleteStatisticResponse(BaseModel):
    message: str
