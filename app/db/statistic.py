import sqlalchemy
from sqlalchemy import Column, Float, Integer, DateTime

from app.db import db

statistic = sqlalchemy.Table(
    "statistic",
    db.metadata,
    Column("date", DateTime, primary_key=True),
    Column("views", Integer),
    Column("clicks", Integer),
    Column("cost", Float),
    Column("cpc", Float),
    Column("cpm", Float),
)
