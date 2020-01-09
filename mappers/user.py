from db.models import User
from forms.user import UserOut, UserIn
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def model2user(model: User) -> UserOut:
    user = UserOut(
        oid=model.id,
        name=model.name,
        email=model.email,
        disabled=model.disabled
    )
    return user


def user2model(user: UserIn, model: User = None) -> User:
    result = model if model else User()
    result.name = user.name
    result.email = user.email
    result.disabled = user.disabled
    if hasattr(user, "password") and user.password:
        result.hashed_password = pwd_context.hash(user.password)
    return result
