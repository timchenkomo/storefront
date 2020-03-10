from pytest import fixture

from db.db import DB_SESSION_LOCAL
from db.models import Base


def truncate_tables(db):
    """Truncate all the data from all the tables."""
    meta = Base.metadata
    for table in reversed(meta.sorted_tables):
        db.execute(table.delete())
        db.commit()


@fixture
def db():
    """Returns DB session."""
    try:
        db = DB_SESSION_LOCAL()
        truncate_tables(db)
        yield db
    finally:
        db.close()
