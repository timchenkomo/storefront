from db import models
from forms.products import Group, Product


def model2product(model: models.Product) -> Product:
    """Creates API form for Product model."""
    return Product(
        type=model.type.name,  # type: ignore
        price=model.price,
        publisher=model.publisher,
        year_published=model.year_published,
        series=model.series.title if model.series else None,
        formats=model.formats.split(";") if model.formats else None,
        slug=model.slug,
        title=model.group.title,
        group_slug=model.group.slug)


def model2group(model: models.Group) -> Group:
    """Creates API form for Group model."""
    products = list(map(model2product, model.products))  # type: ignore
    return Group(
        slug=model.slug,
        title=model.title,
        author=model.author.name,
        description=model.description,
        products=products)


def model2group_nv(model: models.Group) -> Group:
    """Creates API for for Group model."""
    return Group(
        slug=model.slug,
        title=model.title,
        author=model.author.name,
        description=model.description,
        products=[])
