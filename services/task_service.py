from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models.task import Task
from repositories import task_repository
from schemas.task import TaskCreate, TaskPatch, TaskUpdate

def create_task(db: Session, data: TaskCreate, user_id: int):
    return task_repository.create(db, Task(title=data.title, description=data.description, user_id=user_id))

def get_task_or_404(db: Session, task_id: int, user_id: int):
    task = task_repository.get_by_id_for_user(db, task_id, user_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

def list_tasks(db: Session, user_id: int, page: int, page_size: int, completed, sort):
    return task_repository.list_for_user(db, user_id, page, page_size, completed, sort)

def update_task(db: Session, task_id: int, data: TaskUpdate, user_id: int):
    task = get_task_or_404(db, task_id, user_id)
    task.title, task.description, task.completed = data.title, data.description, data.completed
    return task_repository.update(db, task)

def patch_task(db: Session, task_id: int, data: TaskPatch, user_id: int):
    task = get_task_or_404(db, task_id, user_id)
    changes = data.model_dump(exclude_unset=True)
    if not changes:
        raise HTTPException(status_code=400, detail="At least one field is required")
    for field, value in changes.items():
        setattr(task, field, value)
    return task_repository.update(db, task)

def delete_task(db: Session, task_id: int, user_id: int):
    task_repository.delete(db, get_task_or_404(db, task_id, user_id))
