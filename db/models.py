from enum import Enum

from sqlalchemy import Boolean, Column, DateTime
from sqlalchemy import Enum as EnumColumn
from sqlalchemy import ForeignKey, Integer, String, UnicodeText
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()  # pylint: disable=invalid-name


class User(Base):
    """User."""

    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(250), nullable=False)
    email = Column(String(50), nullable=False, index=True)
    hashed_password = Column(String(100), nullable=False)
    disabled = Column(Boolean, nullable=False)

    purchases = relationship("Purchase", back_populates="user", lazy="dynamic")


class Author(Base):
    """Author of a product."""

    __tablename__ = "authors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(128), primary_key=False)

    products = relationship("Group", back_populates="author")


class Series(Base):
    """Series of a product."""

    __tablename__ = "series"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(64), nullable=False)

    products = relationship("Product", back_populates="series")


class Group(Base):
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


class ProductType(Enum):
    """Type of a product."""

    digital = 1
    audio = 2
    printed = 3


class Product(Base):
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
    purchases = relationship("Purchase", back_populates="product")


class Purchase(Base):
    """Purchase."""

    __tablename__ = "purchases"
    id = Column(Integer, primary_key=True, index=True)
    invoice_id = Column(Integer, nullable=False, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)
    product_id = Column(Integer, ForeignKey("products.id"), index=True)
    price = Column(Integer)
    date = Column(DateTime, nullable=False)
    paid = Column(Boolean, nullable=False, default=False)

    product = relationship("Product", back_populates="purchases")
    user = relationship("User", back_populates="purchases")


class AccessToken(Base):
    """Restore password tokens."""
    __tablename__ = "access_token"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)
    token = Column(String(32), index=True, unique=True)
    expiry = Column(DateTime, nullable=False)

    user = relationship("User")
