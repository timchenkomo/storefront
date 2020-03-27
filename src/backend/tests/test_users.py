from datetime import datetime

from starlette.testclient import TestClient

from db.models import User
from forms.auth import Token
from forms.user import SignUp
from main import APP

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
    assert (datetime.utcnow() - user.signup_date).total_seconds() < 10


def test_signin_date_is_null_by_default(db):
    """Last signin date is None before first login."""
    signup_form = SignUp(login="test@test.com", password="123456", name="test das")
    client.post("/api/me/signup", json=signup_form.dict())
    user: User = db.query(User).filter(User.email == "test@test.com").first()
    assert user.last_signin_date is None


def test_update_signin_date(db):
    """Update signin date."""
    signup_form = SignUp(login="test@test.com", password="123456", name="test das")
    signin_form = {"username": "test@test.com", "password": "123456"}

    client.post("/api/me/signup", json=signup_form.dict())
    client.post("/api/me/signin", signin_form)

    user: User = db.query(User).filter(User.email == "test@test.com").first()
    assert user is not None

    # check signup date filled up correctly
    # note: we are using diff between two dates because of lag
    #       between request and response
    assert (datetime.utcnow() - user.last_signin_date).total_seconds() < 10


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


def test_user_able_to_login_afer_registration():
    """User can login after registration."""
    signup_form = SignUp(login="test@test.com", password="123456", name="test das")
    signin_form = {"username": "test@test.com", "password": "123456"}

    response = client.post("/api/me/signup", json=signup_form.dict())
    response = client.post("/api/me/signin", signin_form)
    token: Token = Token(**response.json())

    assert token.token_type == "bearer"
    assert token.access_token is not None


def test_user_unable_to_login_with_invalid_credentials():
    """User unable to login with invalid credentials"""
    signup_form = SignUp(login="test@test.com", password="123456", name="test das")
    signin_form = {"username": "test@test.com", "password": "invalid_password"}

    response = client.post("/api/me/signup", json=signup_form.dict())
    response = client.post("/api/me/signin", signin_form)
    response_data: dict = response.json()

    assert response_data["detail"] == "Incorrect name or password"

