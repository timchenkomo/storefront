from datetime import datetime
from enum import Enum

from sqlalchemy import Boolean, Column, DateTime
from sqlalchemy import Enum as EnumColumn
from sqlalchemy import ForeignKey, Integer, String, UnicodeText
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()  # pylint: disable=invalid-name


class User(Base): # pylint: disable=too-few-public-methods
    """User."""

    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(250), nullable=False)
    email = Column(String(50), nullable=False, index=True)
    hashed_password = Column(String(100), nullable=False)
    disabled = Column(Boolean, nullable=False)
    signup_date = Column(DateTime, nullable=True)
    last_signin_date = Column(DateTime, nullable=True)

    invoices = relationship("Invoice", back_populates="user", lazy="dynamic")


class Author(Base): # pylint: disable=too-few-public-methods
    """Author of a product."""

    __tablename__ = "authors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(128), primary_key=False)

    products = relationship("Group", back_populates="author")


class Series(Base): # pylint: disable=too-few-public-methods
    """Series of a product."""

    __tablename__ = "series"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(64), nullable=False)

    products = relationship("Product", back_populates="series")


class Group(Base): # pylint: disable=too-few-public-methods
    """Group of a products gathered by same title but different types."""

    __tablename__ = "groups"
    id = Column(Integer, primary_key=True, index=True)
    author_id = Column(Integer, ForeignKey("authors.id"), index=True)
    slug = Column(String(32), nullable=False, index=True, unique=True)
    title = Column(String(128), nullable=False)
    description = Column(UnicodeText(), nullable=False)
    cover_url = Column(String(1024), nullable=False)

    author = relationship("Author", back_populates="products")
    products = relationship("Product", back_populates="group")


class ProductType(Enum): # pylint: disable=too-few-public-methods
    """Type of a product."""

    digital = 1
    audio = 2
    printed = 3


class Product(Base): # pylint: disable=too-few-public-methods
    """Specific product."""

    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    group_id = Column(Integer, ForeignKey("groups.id"), index=True)
    series_id = Column(Integer, ForeignKey("series.id"), index=True)
    slug = Column(String(32), nullable=False, index=True, unique=True)

    type = Column(EnumColumn(ProductType), nullable=False)
    price = Column(Integer)
    urls = Column(String(1024))
    publisher = Column(String(256))
    year_published = Column(Integer)

    series = relationship("Series", back_populates="products")
    group = relationship("Group", back_populates="products")


class Invoice(Base): # pylint: disable=too-few-public-methods
    """Invoice."""
    __tablename__ = "invoices"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)
    created_date = Column(DateTime, nullable=False, default=datetime.utcnow)
    paid_date = Column(DateTime, nullable=True)

    user = relationship("User", back_populates="invoices")
    items = relationship("InvoiceItem", back_populates="invoice")


class InvoiceItem(Base): # pylint: disable=too-few-public-methods
    """Invoice item."""
    __tablename__ = "invoice_items"
    id = Column(Integer, primary_key=True, index=True)
    invoice_id = Column(Integer, ForeignKey("invoices.id"), nullable=False, index=True)
    product_id = Column(Integer, ForeignKey("products.id"), index=True)
    price = Column(Integer)

    invoice = relationship("Invoice", back_populates="items")
    product = relationship("Product")


class AccessToken(Base): # pylint: disable=too-few-public-methods
    """Restore password tokens."""
    __tablename__ = "access_tokens"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)
    token = Column(String(32), index=True, unique=True)
    expiry = Column(DateTime, nullable=False)

    user = relationship("User")
