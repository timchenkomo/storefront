from enum import Enum

from sqlalchemy import (Boolean, Column, DateTime, ForeignKey, Integer,
                        String, Table, UnicodeText, Enum as EnumColumn)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(250), nullable=False)
    email = Column(String(50), nullable=False, index=True)
    hashed_password = Column(String(100), nullable=False)
    disabled = Column(Boolean, nullable=False)


class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(128), primary_key=False)

    products = relationship("Product", back_populates="author")


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    author_id = Column(Integer, ForeignKey("authors.id"), index=True)
    slug = Column(String(32), nullable=False, index=True)
    title = Column(String(128), nullable=False)
    description = Column(UnicodeText(), nullable=False)
    cover_url = Column(String(1024), nullable=False)

    author = relationship("Author", back_populates="products")
    varieties = relationship("ProductVariety", back_populates="product")


class ProductType(Enum):
    ebook = 1
    audiobook = 2
    press = 3


class ProductVariety(Base):
    __tablename__ = "product_varieties"
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("products.id"), index=True)
    type = Column(EnumColumn(ProductType))
    price = Column(Integer)
    urls = Column(String(1024))

    product = relationship("Product", back_populates="varieties")
