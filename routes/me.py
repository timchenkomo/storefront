from datetime import timedelta
from typing import Dict

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from auth import (ACCESS_TOKEN_EXPIRE_MINUTES, authenticate_user,
                  create_access_token, get_current_active_user, PWD_CONTEXT)
from db import db_session
from db.models import User
from forms.auth import Token
from forms.products import Group
from forms.user import SignIn, SignUp, UserInfo
from mappers.products import model2group_nv, model2product
from mappers.user import model2user

router = APIRouter() # pylint: disable=invalid-name


@router.post(
    "/signup",
    summary="Register a new user."
)
async def user_signup(
        form: SignUp,
        db: Session = Depends(db_session)):
    """Register a new user."""
    user = User()
    user.name = form.name
    user.email = form.login
    user.hashed_password = PWD_CONTEXT.hash(form.password)
    user.disabled = False
    db.add(user)
    db.commit()
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
    return Token(access_token=access_token, token_type="bearer")


@router.get(
    "/",
    summary="User's data",
    response_model=UserInfo
)
async def user_get_data(
        user: User = Depends(get_current_active_user)) -> UserInfo:
    """Return information about authenticated user."""
    return model2user(user)


@router.get(
    "/products"
)
async def user_get_products(user: User = Depends(get_current_active_user)):
    """Returns list products."""
    result: Dict[int, Group] = {}
    for purchase in user.purchases:  # type: ignore
        product = purchase.product
        product_group = product.group

        if product.id not in result:
            result[product_group.id] = model2group_nv(product_group)

        result[product_group.id].products.append(model2product(product))
    return list(result.values())
