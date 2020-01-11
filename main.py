from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from db.db import engine
from db.models import Base
from routes import me, products

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(me.router, prefix="/me", tags=["me"])
app.include_router(products.router, prefix="/products", tags=["products"])

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
