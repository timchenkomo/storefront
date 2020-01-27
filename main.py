from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from db.db import ENGINE
from db.models import Base
from routes import me, products

Base.metadata.create_all(bind=ENGINE)

APP = FastAPI()
APP.include_router(me.router, prefix="/me", tags=["me"])
APP.include_router(products.router, prefix="/products", tags=["products"])

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
