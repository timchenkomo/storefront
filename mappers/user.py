from db.models import User
from forms.user import UserOutForm


def model2user(model: User) -> UserOutForm:
    return UserOutForm(
        name=model.name,
        email=model.email,
        disabled=model.disabled
    )
