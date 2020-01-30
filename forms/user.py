from typing import Optional

from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel, Schema


class SignUp(BaseModel):
    """SignUp request form."""
    login: str
    password: str
    name: str
    promocode: Optional[str]


class SignIn(OAuth2PasswordRequestForm):
    """SignIn request form."""


class UserInfo(BaseModel):
    """UserInfo response form."""
    name: str = Schema(
        "", title="User's name",
    )
    email: str = ""
    disabled: bool = False


class RestorePasswordRequest(BaseModel):
    """Restore forgotten password."""
    email: str


class ChangePasswordRequest(BaseModel):
    """Change password using specified token."""
    token: str
    password: str
