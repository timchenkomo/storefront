from typing import Optional

from pydantic import BaseModel, Schema


class SignUp(BaseModel):
    login: str
    password: str
    name: str
    promocode: Optional[str]


class SignIn(BaseModel):
    login: str
    password: str


class UserInfo(BaseModel):
    name: str = Schema(
        "", title="User's name",
    )
    email: str = ""
    disabled: bool = False
