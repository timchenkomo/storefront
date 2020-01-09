from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from routes import me
from db.models import Base
from db.db import engine

from api_forms import RegistrationForm, AuthenticationForm

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(me.router, prefix="/me", tags=["me"])

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

USERS = {}


PRODUCTS = [
    {
        "id": 'bg',
        "title": 'Бхагавад-гита как она есть',
        "author": 'А.Ч. Бхактиведанта Свами Прабхупада',
        "cover": 'http://bbt-online.ru/wp-content/uploads/Bhagavad-Gita-2.jpg',
        "description": """Квинтэссенция духовной мудрости Индии и одно из величайших в мире
                        произведений философской классики. Бхагавад-гита дошла до нас в форме
                        диалога Господа Шри Кришны, Личности Бога, и Арджуны, Его близкого друга и
                        преданного, которого Господь обучал науке самоосознания. Поистине, ни одна
                        другая книга не раскрывает так глубоко подлинную природу человека и окружающего
                        мира и отношения человека с Богом.""",
        "varieties": [
            {"id": "bg:digital", "type": "digital", "price": 100, "urls": [
                {"ext": "EPub", "url": "bg.epub", "size": "5 Мб"}, {"ext": "FB2", "url": "bg.fb2", "size": "5 Мб"}]},
            {"id": "bg:audio", "type": "audio", "price": 150, "title": "Аудио",
                "urls": [{"ext": "MP3", "url": "bg.mp3", "size": "1,2 Гб"}]},
            {"id": "bg:printed", "type": "printed",
                "price": 110, "title": "Большая"}
        ]
    },
    {
        "id": 'ns',
        "title": 'Наука самоосознания',
        "author": 'А.Ч. Бхактиведанта Свами Прабхупада',
        "cover": 'http://bbt-online.ru/wp-content/uploads/Nauka-Samoosoznaniya-1.jpg'
    },
    {
        "id": 'vv',
        "title": 'Высший вкус',
        "author": '',
        "cover": 'http://bbt-online.ru/wp-content/uploads/Vysshiy-Vkus-1.jpg'
    },
    {
        "id": 'mh1',
        "title": 'Махабхарата, том первый',
        "author": 'Кришна-дхарма дас',
        "cover": 'http://bbt-online.ru/wp-content/uploads/Mahabharata-1-1.jpg'
    },
    {
        "id": 'mh2',
        "title": 'Махабхарата, том второй',
        "author": 'Кришна-дхарма дас',
        "cover": 'http://bbt-online.ru/wp-content/uploads/Mahabharata-2-1.jpg',
        "desc": '«Махабхарата» Кришна-Дхармы даса представляет собой художественное изложение самой сути одноименного многотомного эпоса. Пересказав сокращенно древнюю поэму, но не упустив при этом ни одной важной детали, автор дает читателю замечательную возможность погрузиться в атмосферу того великого времени, когда на Земле присутствовал Сам Кришна.'
    },
    {
        "id": 'krishna',
        "title": 'Кришна - Верховная личность Бога',
        "author": 'А.Ч. Бхактиведанта Свами Прабхупада',
        "cover": 'http://bbt-online.ru/wp-content/uploads/Krishna-verhovnaya-lichnost-boga.jpg'
    }
]


@app.get("/products")
async def read_products():
    """Returns list of products."""
    return PRODUCTS


@app.get("/products/{product_id}")
async def read_book(product_id: str):
    """Returns specified product."""
    filtered = list(filter(lambda x: x["id"] == product_id, PRODUCTS))
    return filtered[0]


@app.get("/me/products")
async def read_me_products():
    """Returns list products."""
    return PRODUCTS


# USERS

@app.post("/me/signup")
async def user_signup(form: RegistrationForm):
    """Register a new user."""
    USERS[form.login] = form
    return {"success": True}


@app.post("/me/signin")
async def user_signin(form: AuthenticationForm):
    """Authenticate an user using specified credentials."""
    return {"success": True} if form.login in USERS else {"success": False}
