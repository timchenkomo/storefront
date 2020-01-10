from db.models import User
from forms.user import UserOutForm
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def model2user(model: User) -> UserOutForm:
    user = UserOutForm(
        oid=model.id,
        name=model.name,
        email=model.email,
        disabled=model.disabled
    )
    return user
