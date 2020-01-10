from typing import Optional
from pydantic import BaseModel, Schema


class SignUpForm(BaseModel):
    login: str
    password: str
    name: str
    promocode: Optional[str]


class SignInForm(BaseModel):
    login: str
    password: str


class UserInfo(BaseModel):
    name: str = Schema(
        "", title="User's name",
    )
    email: str = ""
    disabled: bool = False
