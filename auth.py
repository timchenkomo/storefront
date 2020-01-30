from datetime import datetime, timedelta
from typing import Optional
from uuid import uuid4

from db import db_session
from db.models import AccessToken, User
from fastapi import Depends, HTTPException, Security
from fastapi.security import OAuth2PasswordBearer
from forms.auth import TokenPayload
from jwt import PyJWTError, decode, encode
from passlib.context import CryptContext  # type: ignore
from sqlalchemy.orm import Session

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
TOKEN_SUBJECT = "access"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
PWD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")
OAUTH2_SCHEME = OAuth2PasswordBearer(tokenUrl="/me/signin")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verifies plain and hashed password to be equal."""
    return PWD_CONTEXT.verify(plain_password, hashed_password)


def get_user(session: Session, login: str) -> User:
    """Returns User by specified login."""
    session.expire_on_commit = False
    return session.query(User).filter_by(email=login).first()


def authenticate_user(
        session: Session,
        login: str,
        password: str) -> Optional[User]:
    """Returns User if the login and password are correct."""
    user = get_user(session, login)
    password_verified = verify_password(password, user.hashed_password)
    return user if user and password_verified else None


def create_access_token(
        *,
        data: dict,
        expires_delta: timedelta = None) -> bytes:
    """Creates JWT token."""
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta if expires_delta else timedelta(minutes=15)
    to_encode.update({"exp": expire, "sub": TOKEN_SUBJECT})
    encoded_jwt = encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(
        token: str = Security(OAUTH2_SCHEME),
        session: Session = Depends(db_session)) -> Optional[User]:
    """Returns current user."""
    try:
        payload = decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        token_data = TokenPayload(**payload)
    except PyJWTError:
        raise HTTPException(status_code=401, detail="Not authenticated")
    return get_user(session, login=token_data.login)


async def get_current_active_user(
        current_user: User = Depends(get_current_user)):
    """Return current active user."""
    if not current_user:
        raise HTTPException(status_code=401, detail="Not authenticated")
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


def create_ot_access_token(user: User, hours: int = 8) -> AccessToken:
    """Create one-time access token for specified user."""
    now = datetime.now()
    delta = timedelta(hours=hours)
    return AccessToken(user=user, token=uuid4().hex, expiry=now + delta)


def find_ot_access_token(db: Session, token: str) -> AccessToken:
    """Find one time access token."""
    now = datetime.now()
    access_token: AccessToken = db.query(AccessToken) \
                                  .filter(
                                      AccessToken.token == token,
                                      AccessToken.expiry > now) \
                                  .first()
    return access_token
