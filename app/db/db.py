from sqlalchemy.engine import URL
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy import create_engine, MetaData
from databases import Database

from app.config import DATABASE


database_url = URL.create(**DATABASE)

database = Database(str(database_url))
metadata = MetaData()

engine = create_engine(database_url)

if not database_exists(engine.url):
    create_database(engine.url)
