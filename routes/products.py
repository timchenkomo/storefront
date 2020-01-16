from fastapi import APIRouter, Depends
from db.models import Group
from db import db_session
from sqlalchemy.orm import Session
from mappers.products import model2group

router = APIRouter()


@router.get(
    "/",
    summary="Returns list of all products."
)
async def get_products(db: Session = Depends(db_session)):
    """Returns list of products."""
    return list(map(model2group, db.query(Group).all()))


@router.get("/{slug}")
async def get_product(slug: str, db: Session = Depends(db_session)):
    """Returns specified product."""
    return model2group(
        db.query(Group).filter(Group.slug == slug).first())
