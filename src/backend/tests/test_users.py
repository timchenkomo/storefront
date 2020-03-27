from datetime import datetime

from forms.auth import Token


def test_register_user_signup_date(signup_user):
    """Checks signup_date is filled up properly after user registration."""
    res, user = signup_user(login="t@t.com", password="123456", name="das")

    assert res.status_code == 200
    assert user is not None

    # check signup date filled up correctly
    # note: we are using diff between two dates because of lag
    #       between request and res
    assert (datetime.utcnow() - user.signup_date).total_seconds() < 10


def test_signin_date_is_null_by_default(signup_user):
    """Last signin date is None before first login."""
    _, user = signup_user(login="t@t.com", password="123456", name="das")
    assert user.last_signin_date is None


def test_update_signin_date(signup_user, signin_user):
    """Update signin date."""
    signup_user(login="t@t.com", password="123456", name="das")
    _, user = signin_user(login="t@t.com", password="123456")

    # check signup date filled up correctly
    # note: we are using diff between two dates because of lag
    #       between request and res
    assert (datetime.utcnow() - user.last_signin_date).total_seconds() < 10


def test_check_user_email_uniqueness(signup_user):
    """Check constraint - email must be unique"""
    res, user = signup_user(login="t@t.com", password="123456", name="das")
    assert res.status_code == 200

    res, user = signup_user(login="t@t.com", password="123456", name="das")
    assert res.status_code == 200
    assert res.json()['msg'] == "Пользователь уже зарегистрирован"


def test_user_able_to_login_afer_registration(signup_user, signin_user):
    """User can login after registration."""
    signup_user(login="t@t.com", password="123456", name="das")
    res, _ = signin_user(login="t@t.com", password="123456")
    token: Token = Token(**res.json())

    assert token.token_type == "bearer"
    assert token.access_token is not None


def test_login_with_invalid_credentials(signup_user, signin_user):
    """User unable to login with invalid credentials"""
    signup_user(login="t@t.com", password="123456", name="das")
    res, _ = signin_user(login="t@t.com", password="iNvAlId")

    assert res.json()["detail"] == "Incorrect name or password"
