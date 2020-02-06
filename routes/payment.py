from os import environ
from hashlib import md5

from db import db_session
from fastapi import APIRouter, Depends, HTTPException, Query

ROOT = environ.get("DOWNLOADS_PATH", "../downloads")
PASS1 = environ.get("MRH_PASS_1", "BJYhRoXsT454wP7aEz5y")
PASS2 = environ.get("MRH_PASS_2", "eJG4iAeXYZ2xMd9Ob4y3")

router = APIRouter()  # pylint: disable=invalid-name


@router.post(
    "/payment",
    summary="Payment callback"
)
async def payment_result(
        out_sum: float = Query(0, alias="OutSum"),
        inv_id: str = Query(None, alias="InvId"),
        crc: str = Query(None, alias="SignatureValue")):
    """Payment callback."""
    my_crc = md5(
        f"{out_sum}:{inv_id}:{PASS1}".encode("utf-8")
    ).hexdigest().upper()
    print(my_crc, crc, f"{out_sum}:{inv_id}:{PASS1}")

    if (my_crc != crc):
        raise HTTPException(status_code=401, detail="Bad sign")

    return {"msg": "Thank you for using our service"}
