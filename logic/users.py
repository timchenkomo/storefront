from typing import List

from sqlalchemy.orm import Session

from db.models import Invoice, InvoiceItem, Product, User


def get_user_products(
        db: Session,
        user: User) -> List[Product]:
    return db.query(Product) \
             .join(InvoiceItem) \
             .join(Invoice)\
             .filter(Invoice.paid_date != None) \
             .filter(User.id == user.id)
