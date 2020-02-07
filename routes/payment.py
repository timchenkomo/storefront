from datetime import datetime
from hashlib import md5
from os import environ
from typing import List

from fastapi import APIRouter, Depends, Form, HTTPException
from sqlalchemy.orm import Session

from auth import get_current_active_user
from db import db_session
from db.models import Product, Purchase, User

PASS1 = environ.get("MRH_PASS_1", "BJYhRoXsT454wP7aEz5y")
PASS2 = environ.get("MRH_PASS_2", "eJG4iAeXYZ2xMd9Ob4y3")
INVOICE_ID_SEQ = 0

router = APIRouter()  # pylint: disable=invalid-name


@router.post(
    "/create"
)
async def payment_create(
        items: List[str],
        user: User = Depends(get_current_active_user),
        db: Session = Depends(db_session)):
    global INVOICE_ID_SEQ
    INVOICE_ID_SEQ = INVOICE_ID_SEQ + 1

    invoice_id = INVOICE_ID_SEQ
    # invoice_id_seq.next_value()
    now = datetime.now()
    for item_slug in items:
        product = db.query(Product).filter(Product.slug == item_slug).first()
        purchase = Purchase(
            invoice_id=invoice_id, paid=False,
            user=user, product=product,
            price=product.price, date=now)
        db.add(purchase)
    db.commit()
    return {"invoice_id": invoice_id}


@router.post(
    "/result_pay",
    summary="Payment callback"
)
async def payment_result(
        out_summ: float = Form(0),
        inv_id: str = Form(None),
        crc: str = Form(None),
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
    db.query(Purchase) \
        .filter(Purchase.invoice_id == inv_id) \
        .update({Purchase.paid: True})
    db.commit()

    return "OK" + inv_id
