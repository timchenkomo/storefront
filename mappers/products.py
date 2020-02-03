from pathlib import Path

from db import models
from forms.products import Group, Product, UrlInfo


def model2url(url: str) -> UrlInfo:
    """Converts url into UrlInfo."""
    ext = ''.join(Path(url).suffixes)
    return UrlInfo(url=url, ext=ext[1:], size="")


def model2product(model: models.Product) -> Product:
    """Creates API form for Product model."""
    urls_def = model.urls or ""
    urls = list(map(model2url, urls_def.split(";")))
    return Product(
        type=model.type.name,  # type: ignore
        price=model.price,
        publisher=model.publisher,
        year_published=model.year_published,
        series=model.series.title if model.series else None,
        urls=urls,
        slug=model.slug)


def model2group(model: models.Group) -> Group:
    """Creates API form for Group model."""
    products = list(map(model2product, model.products))  # type: ignore
    return Group(
        slug=model.slug,
        title=model.title,
        author=model.author.name,
        cover=model.cover_url,
        description=model.description,
        products=products)


def model2group_nv(model: models.Group) -> Group:
    """Creates API for for Group model."""
    return Group(
        slug=model.slug,
        title=model.title,
        author=model.author.name,
        cover=model.cover_url,
        description=model.description,
        products=[])
