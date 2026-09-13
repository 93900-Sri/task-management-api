from sqlalchemy import func, select
from sqlalchemy.orm import Session
from models.task import Task

def create(db: Session, task: Task):
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def get_by_id_for_user(db: Session, task_id: int, user_id: int):
    return db.execute(select(Task).where(Task.id == task_id, Task.user_id == user_id)).scalar_one_or_none()

def list_for_user(db: Session, user_id: int, page: int, page_size: int, completed: bool | None, sort: str):
    conditions = [Task.user_id == user_id]
    if completed is not None:
        conditions.append(Task.completed == completed)
    total = db.execute(select(func.count(Task.id)).where(*conditions)).scalar_one()
    order_column = Task.created_at if sort == "created_at" else Task.id
    statement = select(Task).where(*conditions).order_by(order_column.desc()).offset((page - 1) * page_size).limit(page_size)
    return db.execute(statement).scalars().all(), total

def update(db: Session, task: Task):
    db.commit()
    db.refresh(task)
    return task

def delete(db: Session, task: Task):
    db.delete(task)
    db.commit()
