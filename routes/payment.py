from os import environ
from hashlib import md5
from sqlalchemy.orm import Session
from fastapi import APIRouter, HTTPException, Form, Depends

from db import db_session
from db.models import Product, Purchase, User

PASS1 = environ.get("MRH_PASS_1", "BJYhRoXsT454wP7aEz5y")
PASS2 = environ.get("MRH_PASS_2", "eJG4iAeXYZ2xMd9Ob4y3")

router = APIRouter()  # pylint: disable=invalid-name


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
