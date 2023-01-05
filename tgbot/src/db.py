from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from settings import settings

engine = create_engine('sqlite:///application.sqlite')
session = sessionmaker(bind=engine)

Base = declarative_base()


async def create_db():
    Base.metadata.create_all(engine)
