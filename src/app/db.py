import os

from databases import Database
from sqlalchemy import create_engine, Metadata


DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
metadata = Metadata()

database = Database(DATABASE_URL)
