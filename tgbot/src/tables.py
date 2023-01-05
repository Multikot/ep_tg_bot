import sqlalchemy as sa
from db import Base


class Images(Base):

    __table_name__ = 'images'
    id = sa.Column(sa.BIGINT, primary_key=True)
    name = sa.Column(sa.Text, nullable=False, unique=True)
    descriotion = sa.Column(sa.Text)
    link = sa.Column(sa.Text, nullable=False, unique=True)
    author_tag = sa.Column(sa.Text, nullable=False, unique=True)
