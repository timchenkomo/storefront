from os import environ

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = environ.get(
    "DB_CONNECTION", "postgresql://bbtadm:bbtpass@127.0.0.1/bbt")

ENGINE = create_engine(SQLALCHEMY_DATABASE_URL)
DB_SESSION_LOCAL = sessionmaker(autocommit=False, autoflush=False, bind=ENGINE)


def db_session():
    """Returns DB session."""
    try:
        db = DB_SESSION_LOCAL()
        yield db
    finally:
        db.close()
