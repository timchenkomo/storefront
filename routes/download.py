from os import environ
from os.path import join

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.responses import FileResponse

from auth import get_current_user_by_cookie
from db import db_session
from db.models import Product, Purchase, User

ROOT = environ.get("DOWNLOADS_PATH", "../downloads")

router = APIRouter()  # pylint: disable=invalid-name

# Sample : /sample/{product_slug}.{ext} : {product_slug}/sample.{ext}
# Product: /{product_slug}.{ext}        : {product_slug}/{product_slug}.{ext}
# Reader : /{product_slug}.epub         : {product_slug}/{product_slug}.epub


@router.get(
    "/{product_slug}/sample.{ext}",
    summary="Download a sample of a product."
)
async def download_sample(product_slug: str, ext: str) -> FileResponse:
    """Download a sample."""
    return FileResponse(join(ROOT, product_slug, "sample." + ext))


@router.get(
    "/{product_slug}\.{ext}",  # noqa pylint: disable=W1401
    summary="Download a product."
)
async def download_product(
        product_slug: str,
        ext: str,
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

    return FileResponse(join(ROOT, product_slug, product_slug + "." + ext))
