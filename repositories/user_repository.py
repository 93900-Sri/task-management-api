from sqlalchemy import select
from sqlalchemy.orm import Session
from models.user import User

def get_by_id(db: Session, user_id: int):
    return db.execute(select(User).where(User.id == user_id)).scalar_one_or_none()

def get_by_username(db: Session, username: str):
    return db.execute(select(User).where(User.username == username)).scalar_one_or_none()

def get_by_email(db: Session, email: str):
    return db.execute(select(User).where(User.email == email)).scalar_one_or_none()

def create(db: Session, user: User):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
