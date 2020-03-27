from pytest import fixture
from starlette.testclient import TestClient

from db.db import DB_SESSION_LOCAL
from db.models import Base, User
from forms.user import SignUp
from main import APP


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


@fixture
def client():
    return TestClient(APP)


@fixture
def signup_user(client: TestClient, db):
    def handler(login: str, password: str, name: str, promocode: str = None):
        form = SignUp(login=login, password=password, name=name, promocode=promocode)
        response = client.post("/api/me/signup", json=form.dict())
        user = db.query(User).filter(User.email == form.login).first()
        return response, user
    return handler


@fixture
def signin_user(client: TestClient, db):
    def handler(login: str, password: str):
        form = {"username": login, "password": password}
        response = client.post("/api/me/signin", form)
        user = db.query(User).filter(User.email == login).first()
        return response, user
    return handler
