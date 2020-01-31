from db.models import User
from forms.user import UserInfo


def model2user(model: User) -> UserInfo:
    """Creates API for for User model."""
    products = list(map(lambda x: x.product.slug, model.purchases))

    return UserInfo(
        name=model.name,
        email=model.email,
        disabled=model.disabled,
        products=products
    )
