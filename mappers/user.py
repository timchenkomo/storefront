from db.models import User
from forms.user import UserInfo


def model2user(model: User) -> UserInfo:
    return UserInfo(
        name=model.name,
        email=model.email,
        disabled=model.disabled
    )
