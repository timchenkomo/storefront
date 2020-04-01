#!/usr/local/bin/python

from os import environ
from configparser import ConfigParser
from pathlib import Path

from db.db import db_session
from db.models import Group, Author, Product

print("Scaning for new products")

DOWNLOADS = environ.get("DOWNLOADS_PATH", "../../downloads")

db = next(db_session())  # acquire new db connection


def find_or_create_author(name: str) -> Group:
    author = db.query(Author).filter(Author.name == name).first()
    if not author:
        author = Author(name=name)
    return author


def find_or_create_group(slug: str, author_name: str) -> Group:
    group = db.query(Group).filter(Group.slug == slug).first()
    if not group:
        group = Group(slug=slug)
    group.author = find_or_create_author(author_name)
    return group


def find_or_create_product(slug: str) -> Group:
    product = db.query(Product).filter(Product.slug == slug).first()
    if not product:
        product = Product(slug=slug)
    return product


def proccess_description(text: str) -> str:
    text = text.replace("<br>", "\n")
    return text


# list all directories in /downloads folder
folders = filter(
    lambda x: x.is_dir(),
    Path(DOWNLOADS).iterdir())

# iterate over all directories
for folder in folders:
    config_path = folder.joinpath("config.ini").absolute()

    # skip folder if no config.ini file provided
    if not config_path.exists():
        continue

    config = ConfigParser()
    config.read(config_path)

    # get group info
    group_slug = config.get("group", "slug")
    group_author = config.get("group", "author")
    group = find_or_create_group(group_slug, group_author)
    group.title = config.get("group", "title")
    group.description = proccess_description(config.get("group", "desc"))
    db.add(group)

    # go trought all the sections in config file
    sections = filter(lambda x: x != "group", config.sections())
    for section in sections:
        product_slug = config.get(section, "slug")
        product = find_or_create_product(product_slug)
        product.group = group
        product.type = config.get(section, "type")
        product.price = config.get(section, "price")
        product.publisher = config.get(section, "publisher")
        product.year_published = config.get(section, "year_published")
        product.formats = config.get(section, "formats")
        db.add(product)

        print(group, group.title, product_slug, product.type, product.price)


db.commit()

    # group_exist = folder.name in group_titles
    # print(folder.name, group_exist)


#for group in groups:
#    print(group.title)

