from starlette.middleware.cors import CORSMiddleware

from db.db import ENGINE
from db.models import Base
from fastapi import FastAPI
from routes import download, me, products

Base.metadata.create_all(bind=ENGINE)

APP = FastAPI()
APP.include_router(me.router, prefix="/api/me", tags=["me"])
APP.include_router(products.router, prefix="/api/products", tags=["products"])
APP.include_router(download.router, prefix="/api/download", tags=["download"])

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
