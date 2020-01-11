from typing import List

from pydantic import BaseModel


class UrlInfo(BaseModel):
    """Additional information to URL for specific product variety."""
    ext: str
    url: str
    size: str


class ProductVariety(BaseModel):
    """Specific variety of a product."""
    id: str
    type: str
    price: int
    urls: List[UrlInfo]


class Product(BaseModel):
    """Product."""
    slug: str
    title: str
    author: str
    cover: str
    description: str
    varieties: List[ProductVariety]
