from pathlib import Path

from forms.products import Group, Product, UrlInfo


def model2url(url) -> UrlInfo:
    ext = ''.join(Path(url).suffixes)
    return UrlInfo(url=url, ext=ext, size="")


def model2product(model) -> Product:
    urls = list(map(model2url, model.urls.split(";")))
    return Product(
        id=model.id,
        type=model.type.name,
        price=model.price,
        publisher=model.publisher,
        year_published=model.year_published,
        series=model.series.title if model.series else None,
        urls=urls)


def model2group(model) -> Group:
    products = list(map(model2product, model.products))
    return Group(
        slug=model.slug,
        title=model.title,
        author=model.author.name,
        cover=model.cover_url,
        description=model.description,
        products=products)


def model2groupNV(model) -> Group:
    return Group(
        slug=model.slug,
        title=model.title,
        author=model.author.name,
        cover=model.cover_url,
        description=model.description,
        products=[])
