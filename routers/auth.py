from fastapi import APIRouter,Depends,HTTPException,status

from sqlalchemy.orm import Session

from database import get_db
from models import User
from schemas import UserCreate,UserLogin,UserResponse

import crud

from security import(hash_password,
                    verify_password,
                    create_access_token,
                    get_current_user,
                    oauth2_scheme)

router=APIRouter(prefix="/users",
                 tags=["Users"])




@router.post("/register")
def register_user(user:UserCreate,db:Session=Depends(get_db)):

    existing_user=crud.get_user_by_username(db,user.username)
    if existing_user :
        raise HTTPException(status_code=400,detail="Username already exists")
    
    existing_email=crud.get_user_by_email(db,user.email)

    if existing_email:
        raise HTTPException(status_code=400,detail="Email already exists")

    hashed_password=hash_password(user.password)
    
    new_user=crud.create_user(db,
                              username=user.username,
                              email=user.email,
                              password=hashed_password)
    return new_user

@router.post("/login")
def login_user(user:UserLogin,
               db:Session=Depends(get_db)):

    existing_user=crud.get_user_by_email(db,user.email)
    
    

    if not existing_user:
        raise HTTPException(status_code=401,detail="Invalid Email or password")
    # return {"message":"User found"}

    if not verify_password(user.password,existing_user.password):
        raise HTTPException(status_code=401,detail="Invalid email or password")
    
    # return {"message":"Login successful"}

    access_token=create_access_token({"user_id":existing_user.id})
    return {"access_token":access_token,
            "token_type":"bearer"}

# jwt token
@router.get("/me")
def get_me(token:str=Depends(oauth2_scheme),
           db:Session=Depends(get_db)):
    user_id=get_current_user(token)
    user=db.query(User).filter(User.id==user_id).first()
    if not user:
        raise HTTPException(status_code=404,detail="User not found")
    return{
        "id":user.id,
        "username":user.username,
        "email":user.email
    }