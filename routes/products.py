from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db import db_session
from db.models import Group, Product
from mappers.products import model2group, model2product

router = APIRouter()  # pylint: disable=invalid-name


@router.get(
    "/products",
    summary="Returns list of all products."
)
async def get_groups(db: Session = Depends(db_session)):
    """Returns list of products."""
    return list(map(model2group, db.query(Group).all()))


@router.get("/products/{slug}")
async def get_group(slug: str, db: Session = Depends(db_session)):
    """Returns specified product."""
    return model2group(
        db.query(Group).filter(Group.slug == slug).first())


@router.get(
    "/product/{slug}"
)
async def get_product(slug: str, db: Session = Depends(db_session)):
    return model2product(
        db.query(Product).filter(Product.slug == slug).first())
