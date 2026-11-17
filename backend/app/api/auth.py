from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.schemas.user import UserCreate, Token
from app.core.security import get_password_hash, verify_password, create_access_token

# Здесь будут импорты моделей и подключения к БД (ожидаем от У2)
# from app.api.deps import get_db
# from app.models.user import User

router = APIRouter()


@router.post("/register", response_model=Token, status_code=status.HTTP_201_CREATED)
def register(user_in: UserCreate, db: Session = Depends(get_db)):
    # 1. Проверить, есть ли уже такой email в БД
    # user = db.query(User).filter(User.email == user_in.email).first()
    # if user:
    #     raise HTTPException(status_code=400, detail="Email already registered")

    # 2. Создать нового пользователя с хешированным паролем
    # new_user = User(email=user_in.email, hashed_password=get_password_hash(user_in.password))
    # db.add(new_user)
    # db.commit()
    # db.refresh(new_user)

    # 3. Сгенерировать токен
    # access_token = create_access_token(data={"sub": new_user.email})
    # return {"access_token": access_token, "token_type": "bearer"}
    pass  # Удалить pass, когда код будет раскомментирован


@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # 1. Найти пользователя по email
    # user = db.query(User).filter(User.email == form_data.username).first()
    # if not user or not verify_password(form_data.password, user.hashed_password):
    #     raise HTTPException(status_code=401, detail="Incorrect email or password")

    # 2. Вернуть токен
    # access_token = create_access_token(data={"sub": user.email})
    # return {"access_token": access_token, "token_type": "bearer"}
    pass