from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from routes import download, me, payment, products

APP = FastAPI()
APP.include_router(me.router, prefix="/api/me", tags=["me"])
APP.include_router(products.router, prefix="/api", tags=["products"])
APP.include_router(download.router, prefix="/api/download", tags=["download"])
APP.include_router(payment.router, prefix="/api/payment", tags=["payment"])

ORIGINS = [
    "http://localhost",
    "http://localhost:3000",
    "http://bbt-online.ru"
]

APP.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
