from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app.api import tasks as tasks_router
from app.models import user, task, category

Base.metadata.create_all(bind=engine)

app = FastAPI(title="ToDo List API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключаем роутер для задач
app.include_router(tasks_router.router, prefix="/api/tasks", tags=["tasks"])

@app.get("/")
def read_root():
    return {"message": "Welcome to ToDo List API. Go to /docs for Swagger UI."}
