from datetime import datetime
from hashlib import md5
from os import environ
from typing import List

from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session

from auth import get_current_active_user
from db import db_session
from db.models import Invoice, InvoiceItem, Product, User

PASS1 = environ.get("MRH_PASS_1", "BJYhRoXsT454wP7aEz5y")
PASS2 = environ.get("MRH_PASS_2", "eJG4iAeXYZ2xMd9Ob4y3")

router = APIRouter()  # pylint: disable=invalid-name


@router.post(
    "/create"
)
async def payment_create(
        items: List[str],
        user: User = Depends(get_current_active_user),
        db: Session = Depends(db_session)):
    """Create a new invoice."""
    invoice = Invoice(user=user)

    for item_slug in items:
        product = db.query(Product).filter(Product.slug == item_slug).first()
        if not product:
            raise HTTPException(status_code=400, detail=f"No '{item_slug}' product found")
        InvoiceItem(invoice=invoice, product=product, price=product.price)

    db.add(invoice)
    db.commit()
    return {"invoice_id": invoice.id}


@router.get(
    "/result_pay",
    summary="Payment callback"
)
async def payment_result(
        out_summ: float = Query(0),
        inv_id: str = Query(None),
        crc: str = Query(None),
        db: Session = Depends(db_session)):
    """Payment callback."""
    # truncate zeros from the end
    out_summ2 = str(round(out_summ)).rstrip('0').rstrip('.')
    my_crc = md5(
        f"{out_summ2}:{inv_id}:{PASS2}".encode("utf-8")
    ).hexdigest().upper()

    if (my_crc != crc):
        raise HTTPException(status_code=401, detail="Bad sign")

    # update flag
    db.query(Invoice) \
        .filter(Invoice.id == inv_id) \
        .update({Invoice.paid_date: datetime.utcnow()})
    db.commit()

    return "OK" + inv_id
