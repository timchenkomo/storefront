from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

ENGINE = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
DB_SESSION_LOCAL = sessionmaker(autocommit=False, autoflush=False, bind=ENGINE)


def db_session():
    """Returns DB session."""
    try:
        db = DB_SESSION_LOCAL()
        yield db
    finally:
        db.close()
