from typing import List, Optional

from pydantic import BaseModel


class UrlInfo(BaseModel):
    """Additional information to URL for specific product."""
    ext: str
    url: str
    size: str


class Product(BaseModel):
    """Specific product."""
    id: str
    type: str
    price: int
    publisher: Optional[str]
    year_published: Optional[int]
    series: Optional[str]
    urls: List[UrlInfo]


class Group(BaseModel):
    """Products gorup."""
    slug: str
    title: str
    author: str
    cover: str
    description: str
    products: List[Product]
