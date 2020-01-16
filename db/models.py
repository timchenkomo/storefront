from enum import Enum

from sqlalchemy import Boolean, Column, DateTime
from sqlalchemy import Enum as EnumColumn
from sqlalchemy import ForeignKey, Integer, String, UnicodeText
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(250), nullable=False)
    email = Column(String(50), nullable=False, index=True)
    hashed_password = Column(String(100), nullable=False)
    disabled = Column(Boolean, nullable=False)

    purchases = relationship("Purchase", back_populates="user")


class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(128), primary_key=False)

    products = relationship("Group", back_populates="author")


class Series(Base):
    __tablename__ = "series"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(64), nullable=False)

    products = relationship("Product", back_populates="series")


class Group(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True, index=True)
    author_id = Column(Integer, ForeignKey("authors.id"), index=True)
    slug = Column(String(32), nullable=False, index=True)
    title = Column(String(128), nullable=False)
    description = Column(UnicodeText(), nullable=False)
    cover_url = Column(String(1024), nullable=False)

    author = relationship("Author", back_populates="products")
    products = relationship("Product", back_populates="group")


class ProductType(Enum):
    digital = 1
    audio = 2
    printed = 3


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    group_id = Column(Integer, ForeignKey("groups.id"), index=True)
    series_id = Column(Integer, ForeignKey("series.id"), index=True)
    type = Column(EnumColumn(ProductType))
    price = Column(Integer)
    urls = Column(String(1024))

    publisher = Column(String(256))
    year_published = Column(Integer)

    series = relationship("Series", back_populates="products")
    group = relationship("Group", back_populates="products")
    purchases = relationship("Purchase", back_populates="product")


class Purchase(Base):
    __tablename__ = "purchases"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True)
    product_id = Column(Integer, ForeignKey("products.id"), index=True)
    price = Column(Integer)
    date = Column(DateTime, nullable=False)

    product = relationship("Product", back_populates="purchases")
    user = relationship("User", back_populates="purchases")
