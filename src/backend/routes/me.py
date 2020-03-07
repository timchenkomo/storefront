from datetime import timedelta, datetime
from typing import Dict, List

from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException
from sqlalchemy.orm import Session

from auth import (ACCESS_TOKEN_EXPIRE_MINUTES, PWD_CONTEXT, authenticate_user,
                  create_access_token, create_ot_access_token,
                  find_ot_access_token, get_current_active_user)
from db import db_session
from db.models import AccessToken, Product, User
from forms.auth import Token
from forms.products import Group
from forms.user import (ChangePasswordRequest, RestorePasswordRequest, SignIn,
                        SignUp, UserInfo)
from logic.users import get_user_products
from mappers.products import model2group_nv, model2product
from mappers.user import model2user
from postman import send_change_password_email, send_welcome_email

router = APIRouter()  # pylint: disable=invalid-name


@router.post(
    "/signup",
    summary="Register a new user."
)
async def user_signup(
        form: SignUp,
        task: BackgroundTasks,
        db: Session = Depends(db_session)):
    """Register a new user."""
    user = User()
    user.name = form.name
    user.email = form.login
    user.hashed_password = PWD_CONTEXT.hash(form.password)
    user.disabled = False
    db.add(user)
    db.commit()
    task.add_task(send_welcome_email, user.email)
    return {"success": True}


@router.post(
    "/signin",
    summary="Sign user in and returns token back.",
    response_model=Token)
async def user_signin(
        credentials: SignIn = Depends(),
        db: Session = Depends(db_session)) -> Token:
    """Authenticate user using specified credentials."""
    user = authenticate_user(db, credentials.username, credentials.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect name or password")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"login": user.email}, expires_delta=access_token_expires)
    user.last_signin_date = datetime.now()
    db.add(user)
    db.commit()
    return Token(access_token=access_token, token_type="bearer")


@router.get(
    "/",
    summary="User's data",
    response_model=UserInfo
)
async def user_get_data(
        user: User = Depends(get_current_active_user),
        db: Session = Depends(db_session)) -> UserInfo:
    """Return information about authenticated user."""
    return model2user(user, db)


@router.get(
    "/products"
)
async def user_get_products(
        user: User = Depends(get_current_active_user),
        db: Session = Depends(db_session)):
    """Returns list products."""
    result: Dict[int, Group] = {}
    products: List[Product] = get_user_products(db, user)
    for product in products:  # type: ignore
        product_group = product.group

        if product_group.id not in result:
            result[product_group.id] = model2group_nv(product_group)

        result[product_group.id].products.append(model2product(product))
    return list(result.values())


@router.post(
    "/password/restore"
)
async def user_restore_password(
        form: RestorePasswordRequest,
        tasks: BackgroundTasks,
        db: Session = Depends(db_session)):
    """Sends a restore email to user."""
    user: User = db.query(User).filter(User.email == form.email).first()
    if not user:
        return {"success": False, "msg": "No user found"}

    # generate token
    token = create_ot_access_token(user)
    db.add(token)
    db.commit()

    # send email
    tasks.add_task(send_change_password_email, user.email, token=token.token)

    return {"success": True}


@router.post(
    "/password/change"
)
async def user_change_password(
        form: ChangePasswordRequest,
        db: Session = Depends(db_session)):
    """Change password for user."""
    token: AccessToken = find_ot_access_token(db, form.token)
    if not token:
        return {"success": False, "msg": "Token was not found"}

    token.user.hashed_password = PWD_CONTEXT.hash(form.password)
    db.delete(token)
    db.commit()
    return {"success": True}
