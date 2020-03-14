from starlette.testclient import TestClient

from main import APP
from forms.user import SignUp
from db.models import User
from datetime import datetime

client = TestClient(APP)


def test_register_user_signup_date(db):
    """Checks signup_date is filled up properly after user registration."""
    # register a new user
    form = SignUp(login="test@test.com", password="123456", name="test das")
    response = client.post("/api/me/signup", json=form.dict())
    assert response.status_code == 200

    # find user in db
    user: User = db.query(User).filter(User.email == "test@test.com").first()
    assert user is not None

    # check signup date filled up correctly
    # note: we are using diff between two dates because of lag
    #       between request and response
    assert (datetime.now() - user.signup_date).total_seconds() < 10

def test_check_user_email_uniqueness(db):
    """Check constraint - email must be unique"""
    # register a new user
    form = SignUp(login="test@test.com", password="123456", name="test das")
    response = client.post("/api/me/signup", json=form.dict())
    assert response.status_code == 200
    # register same user 
    form = SignUp(login="test@test.com", password="123456", name="test das")
    response = client.post("/api/me/signup", json=form.dict())
    assert response.status_code == 200
    dataJson = response.json()
    assert dataJson['msg'] == "Пользователь уже зарегистрирован"


    

