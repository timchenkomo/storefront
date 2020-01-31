from os import environ
from os.path import join

from starlette.responses import FileResponse

from auth import get_current_user_by_cookie
from db import db_session
from db.models import Product, Purchase, User
from fastapi import APIRouter, Cookie, Depends, HTTPException, Security
from fastapi.security import APIKeyCookie
from sqlalchemy.orm import Session

ROOT = environ.get("DOWNLOADS_PATH", "../downloads")

router = APIRouter()  # pylint: disable=invalid-name



@router.get(
    "/{product_slug}/sample_{filename}",
    summary="Download a sample of a product."
)
async def download_sample(product_slug: str, filename: str) -> FileResponse:
    """Download a sample."""
    return FileResponse(join(ROOT, product_slug, "sample_" + filename))


@router.get(
    "/{product_slug}/{filename}",
    summary="Download a product."
)
async def download_product(
        product_slug: str,
        filename: str,
        user: User = Depends(get_current_user_by_cookie),
        db: Session = Depends(db_session)) -> FileResponse:
    """Download a product file if user have bought it."""
    # Check if product exists
    product = db.query(Product).filter(Product.slug == product_slug).first()
    if not product:
        raise HTTPException(status_code=404, detail="No product found")

    # Has the user bought it before?
    purchase = db.query(Purchase).filter(
        Purchase.user_id == user.id, Purchase.product_id == product.id) \
        .first()
    if not purchase:
        raise HTTPException(status_code=403, detail="Doesn't belong to you")

    return FileResponse(join(ROOT, product.group.slug, filename))
