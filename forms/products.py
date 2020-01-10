from pydantic import BaseModel
from typing import List


class UrlInfo(BaseModel):
    """Additional information to URL for specific product variety."""
    ext: str
    url: str
    size: str


class ProductVariety(BaseModel):
    """Specific variety of a product."""
    vid: str
    type: str
    price: int
    urls: List[UrlInfo]


class Product(BaseModel):
    """Product."""
    pid: str
    title: str
    author: str
    cover: str
    description: str
    varieties: List[ProductVariety]
