from typing import Literal
from fastapi import APIRouter, Depends, Query, Response, status
from sqlalchemy.orm import Session
from database.conn import get_db
from models.user import User
from schemas.task import TaskCreate, TaskListResponse, TaskPatch, TaskResponse, TaskUpdate
from security.jwt import get_current_user
from services import task_service

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.post("", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
def create_task(data: TaskCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return task_service.create_task(db, data, current_user.id)

@router.get("", response_model=TaskListResponse)
def list_tasks(page: int = Query(1, ge=1), page_size: int = Query(10, ge=1, le=100), completed: bool | None = Query(None), sort: Literal["id", "created_at"] = Query("id"), db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    items, total = task_service.list_tasks(db, current_user.id, page, page_size, completed, sort)
    return {"items": items, "total": total, "page": page, "page_size": page_size}

@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return task_service.get_task_or_404(db, task_id, current_user.id)

@router.put("/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, data: TaskUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return task_service.update_task(db, task_id, data, current_user.id)

@router.patch("/{task_id}", response_model=TaskResponse)
def patch_task(task_id: int, data: TaskPatch, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return task_service.patch_task(db, task_id, data, current_user.id)

@router.patch("/{task_id}/complete", response_model=TaskResponse)
def complete_task(task_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    task = task_service.get_task_or_404(db, task_id, current_user.id)
    task.completed = True
    return task_service.update_task(db, task_id, TaskUpdate(title=task.title, description=task.description, completed=True), current_user.id)

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    task_service.delete_task(db, task_id, current_user.id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
