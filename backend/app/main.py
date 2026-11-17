from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base

# Импортируем модели, чтобы SQLAlchemy знал о них при создании таблиц
from app.models import user, task, category

# Создаем таблицы в базе данных (если их еще нет)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="ToDo List API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to ToDo List API. Go to /docs for Swagger UI."}
