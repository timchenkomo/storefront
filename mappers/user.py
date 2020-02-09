from typing import List

from db.models import Product, User
from forms.user import UserInfo
from logic.users import get_user_products


def model2user(model: User, db) -> UserInfo:
    """Creates API for for User model."""
    # convert all the purcahes to the list of product slugs
    products: List[Product] = get_user_products(db, model)
    product_slugs: List[str] = list(map(lambda x: x.product.slug, products))

    return UserInfo(
        name=model.name,
        email=model.email,
        disabled=model.disabled,
        products=product_slugs
    )
