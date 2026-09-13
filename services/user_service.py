from fastapi import HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from models.user import User
from repositories import user_repository
from schemas.user import UserCreate
from security.password import hash_password, verify_password
from security.jwt import create_access_token

def register_user(db: Session, data: UserCreate):
    if user_repository.get_by_username(db, data.username):
        raise HTTPException(status_code=409, detail="Username already exists")
    if user_repository.get_by_email(db, data.email):
        raise HTTPException(status_code=409, detail="Email already exists")
    user = User(username=data.username, email=data.email, password_hash=hash_password(data.password))
    try:
        return user_repository.create(db, user)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409, detail="Username or email already exists")

def login_user(db: Session, username: str, password: str):
    user = user_repository.get_by_username(db, username)
    if user is None or not verify_password(password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid username or password", headers={"WWW-Authenticate": "Bearer"})
    return create_access_token(user.id)
