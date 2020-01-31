from typing import List

from db.models import Purchase, User
from forms.user import UserInfo


def model2user(model: User) -> UserInfo:
    """Creates API for for User model."""
    # convert all the purcahes to the list of product slugs
    purchases: List[Purchase] = list(model.purchases)  # type: ignore
    products: List[str] = list(map(lambda x: x.product.slug, purchases))

    return UserInfo(
        name=model.name,
        email=model.email,
        disabled=model.disabled,
        products=products
    )
