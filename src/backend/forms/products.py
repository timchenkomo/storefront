from typing import List, Optional

from pydantic import BaseModel


class Product(BaseModel):
    """Specific product."""
    type: str
    slug: str
    price: int
    publisher: Optional[str]
    year_published: Optional[int]
    series: Optional[str]
    formats: Optional[List[str]]
    sample_formats: Optional[List[str]]
    title: Optional[str]
    group_slug: Optional[str]


class Group(BaseModel):
    """Products gorup."""
    slug: str
    title: str
    author: str
    description: str
    products: List[Product]
