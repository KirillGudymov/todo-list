from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

from app.database import SessionLocal
from app.models.task import Task
from app.models.user import User # Пока просто для связи

router = APIRouter()

# Схема данных для создания/обновления задачи (Pydantic)
class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    category_id: Optional[int] = None
    due_date: Optional[datetime] = None

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[bool] = None
    category_id: Optional[int] = None
    due_date: Optional[datetime] = None

class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    status: bool
    due_date: Optional[datetime] = None
    category_id: Optional[int] = None
    user_id: int

    class Config:
        orm_mode = True

# Зависимость для получения сессии БД
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Временная заглушка, так как авторизацию мы пока не трогаем
# В реальности здесь будет браться текущий пользователь из токена
def get_current_user():
    return {"id": 1} 

@router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    new_task = Task(
        title=task.title,
        description=task.description,
        category_id=task.category_id,
        due_date=task.due_date,
        user_id=current_user["id"]
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

@router.get("/", response_model=List[TaskResponse])
def get_tasks(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    # Пока возвращаем все задачи (позже добавим фильтрацию по user_id)
    tasks = db.query(Task).all()
    return tasks

@router.put("/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task_update: TaskUpdate, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    if task_update.title is not None:
        task.title = task_update.title
    if task_update.description is not None:
        task.description = task_update.description
    if task_update.status is not None:
        task.status = task_update.status
    if task_update.category_id is not None:
        task.category_id = task_update.category_id
    if task_update.due_date is not None:
        task.due_date = task_update.due_date

    db.commit()
    db.refresh(task)
    return task

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    db.delete(task)
    db.commit()
    return None
