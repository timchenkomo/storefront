from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from auth import (ACCESS_TOKEN_EXPIRE_MINUTES, authenticate_user,
                  create_access_token, get_current_active_user, pwd_context)
from db import db_session
from db.models import User
from forms.auth import Token
from forms.user import SignUp, SignIn, UserInfo
from mappers.user import model2user
from mappers.products import model2productNV, model2variety


router = APIRouter()


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
    user.hashed_password = pwd_context.hash(form.password)
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
    return {"access_token": access_token, "token_type": "bearer"}


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
    result = {}
    for purchase in user.purchases:
        product_variety = purchase.product_variety
        product = product_variety.product

        if product.id not in result:
            result[product.id] = model2productNV(product)

        result[product.id].varieties.append(model2variety(product_variety))
    return list(result.values())
