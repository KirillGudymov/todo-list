from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="ToDo List API", version="1.0.0")

# Настройка CORS (чтобы фронтенд мог делать запросы)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Для продакшена лучше указать конкретный домен
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to ToDo List API. Go to /docs for Swagger UI."}