from fastapi import APIRouter, Depends
from db.models import Product
from db import db_session
from sqlalchemy.orm import Session
from mappers.products import model2product

router = APIRouter()


@router.get(
    "/",
    summary="Returns list of all products."
)
async def read_products(db: Session = Depends(db_session)):
    """Returns list of products."""
    return list(map(model2product, db.query(Product).all()))


@router.get("/{slug}")
async def read_book(slug: str, db: Session = Depends(db_session)):
    """Returns specified product."""
    return model2product(db.query(Product).filter(Product.slug == slug).first())


#@router.get("/me/products")
#async def read_me_products():
#    """Returns list products."""
#    return PRODUCTS
