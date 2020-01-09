from pydantic import BaseModel
from typing import Optional, List


# USERS

class RegistrationForm(BaseModel):
    login: str
    password: str
    promocode: Optional[str]


class AuthenticationForm(BaseModel):
    login: str
    password: str


# PRODUCTS

class UrlInfo:
    """Additional information to URL for specific product variety."""
    ext: str
    url: str
    size: str


class ProductVariety:
    """Specific variety of a product."""
    vid: str
    type: str
    price: int
    urls: List[UrlInfo]


class Product:
    """Product."""
    pid: str
    title: str
    author: str
    cover: str
    description: str
    varieties: List[ProductVariety]
