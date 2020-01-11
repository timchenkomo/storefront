from forms.products import Product, ProductVariety, UrlInfo


def model2url(url) -> UrlInfo:
    return UrlInfo(url=url, ext="123", size="123")


def model2variety(model) -> ProductVariety:
    urls = list(map(model2url, model.urls.split(",")))
    return ProductVariety(
        id=model.id,
        type=model.type.name,
        price=model.price,
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
