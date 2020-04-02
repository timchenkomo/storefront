#!/usr/local/bin/python

from configparser import ConfigParser
from os import environ
from pathlib import Path

from db.db import db_session
from db.models import Author, Group, Product

print("Scaning for new products")

DOWNLOADS = environ.get("DOWNLOADS_PATH", "../../downloads")
GROUPS = []
PRODUCTS = []
DELETE_UNLISTED = False

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
    print(f"Processing {folder}")
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

    # check slug and folder name are equal
    if folder.name != group_slug:
        raise Exception(f"Folder name and group slug mismatch for {folder.name} != {group_slug}")

    # check cover exists
    if not folder.joinpath("cover.jpg").exists():
        raise Exception(f"No cover found for {folder}")

    # add groups
    db.add(group)
    GROUPS.append(group_slug)

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
        product.sample_formats = config.get(section, "sample_formats", fallback=None)

        # check files exists
        files_are_present = map(
            lambda fmt: folder.joinpath(product.slug + "." + fmt).exists(),
            product.formats.split(";"))
        if not all(files_are_present):
            raise Exception(f"Not all files are present for {folder}")

        # check sample files exists
        if product.sample_formats:
            samples_are_present = map(
                lambda fmt: folder.joinpath(product.slug + ".sample." + fmt).exists(),
                product.sample_formats.split(";"))
            if not all(samples_are_present):
                raise Exception(f"Not all sample files are present for {folder}")

        # add product
        db.add(product)
        PRODUCTS.append(product_slug)


# Delete unlisted products
if DELETE_UNLISTED:
    all_products = db.query(Product).all()
    all_groups = db.query(Group).all()
    del_products = list(filter(lambda p: p.slug not in PRODUCTS, all_products))

    del_products = list(filter(lambda p: p.slug not in PRODUCTS, all_products))
    del_groups = list(filter(lambda p: p.slug not in GROUPS, all_groups))

    for product in del_products:
        print(f"Delete {product.slug} {product.type}. {PRODUCTS}")
        db.delete(product)

        for group in del_groups:
            print(f"Delete {group.slug} {group}")
            db.delete(group)

db.commit()
