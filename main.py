from starlette.middleware.cors import CORSMiddleware

from db.db import ENGINE
from db.models import Base
from fastapi import FastAPI
from routes import download, me, products

Base.metadata.create_all(bind=ENGINE)

APP = FastAPI()
APP.include_router(me.router, prefix="/me", tags=["me"])
APP.include_router(products.router, prefix="/products", tags=["products"])
APP.include_router(download.router, prefix="/download", tags=["download"])

ORIGINS = [
    "http://localhost",
    "http://localhost:3000",
]

APP.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
