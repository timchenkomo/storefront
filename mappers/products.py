from pathlib import Path

from forms.products import Product, ProductVariety, UrlInfo


def model2url(url) -> UrlInfo:
    ext = ''.join(Path(url).suffixes)
    return UrlInfo(url=url, ext=ext, size="")


def model2variety(model) -> ProductVariety:
    urls = list(map(model2url, model.urls.split(";")))
    return ProductVariety(
        id=model.id,
        type=model.type.name,
        price=model.price,
        publisher=model.publisher,
        year_published=model.year_published,
        series=model.series.title if model.series else None,
        urls=urls)


def model2product(model) -> Product:
    varieties = list(map(model2variety, model.varieties))
    return Product(
        slug=model.slug,
        title=model.title,
        author=model.author.name,
        cover=model.cover_url,
        description=model.description,
        varieties=varieties)


def model2productNV(model) -> Product:
    return Product(
        slug=model.slug,
        title=model.title,
        author=model.author.name,
        cover=model.cover_url,
        description=model.description,
        varieties=[])
