import uuid

from sqlalchemy import Column, DateTime, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from sqlalchemy.sql.sqltypes import Integer

from articles_app.db.connector import ENGINE

Base = declarative_base()


# class Customer(Base):
#     __tablename__ = "articles"
#     id = Column(
#         String,
#         primary_key=True,
#         unique=True,
#         nullable=False,
#         default=lambda: str(uuid.uuid4()),
#     )

#     first_name = Column(String, nullable=False)
#     last_name = Column(String, nullable=False)


class Article(Base):
    __tablename__ = "articles"
    id = Column(
        String,
        primary_key=True,
        unique=True,
        nullable=False,
        default=lambda: str(uuid.uuid4()),
    )
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    quantity = Column(Integer, default=0)


def configure_database():
    Article.__table__.drop(ENGINE.engine)
    Base.metadata.create_all(ENGINE.engine)


if __name__ == "__main__":
    configure_database()
