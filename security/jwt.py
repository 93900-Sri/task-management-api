from datetime import datetime, timedelta, timezone
import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jwt.exceptions import InvalidTokenError
from sqlalchemy.orm import Session
from database.conn import get_db, settings
from repositories import user_repository

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/users/login")

def create_access_token(user_id: int):
    now = datetime.now(timezone.utc)
    payload = {"sub": str(user_id), "iat": now, "exp": now + timedelta(minutes=settings.access_token_expire_minutes)}
    return jwt.encode(payload, settings.jwt_secret_key, algorithm=settings.jwt_algorithm)

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    error = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication credentials", headers={"WWW-Authenticate": "Bearer"})
    try:
        payload = jwt.decode(token, settings.jwt_secret_key, algorithms=[settings.jwt_algorithm])
    except InvalidTokenError:
        raise error
    subject = payload.get("sub")
    if subject is None:
        raise error
    try:
        user_id = int(subject)
    except (TypeError, ValueError):
        raise error
    user = user_repository.get_by_id(db, user_id)
    if user is None:
        raise error
    return user
