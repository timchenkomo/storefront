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


class UserOutForm(BaseModel):
    name: str = Schema(
        "", title="User's name",
        min_length=3, max_length=128
    )
    email: str = ""
    disabled: bool = False
