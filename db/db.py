from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://bbtadm:bbtpass@postgres/bbt"

ENGINE = create_engine(SQLALCHEMY_DATABASE_URL)
DB_SESSION_LOCAL = sessionmaker(autocommit=False, autoflush=False, bind=ENGINE)


def db_session():
    """Returns DB session."""
    try:
        db = DB_SESSION_LOCAL()
        yield db
    finally:
        db.close()
