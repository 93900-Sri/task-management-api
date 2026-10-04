from pydantic import BaseModel


class TaskCreate(BaseModel):
    title:str
    description:str
    completed:bool=False

class TaskUpdate(BaseModel):
    title:str | None=None
    description:str | None=None
    completed:bool|None=None

class TaskPatch(BaseModel):
    title:str | None=None
    description:str | None=None
    completed:bool|None=None

class UserCreate(BaseModel):
    username:str
    email:str
    password:str

class UserLogin(BaseModel):
    email:str
    password:str

class TaskResponse(BaseModel):
    id:int
    title:str
    description:str
    completed:bool
    user_id:int

    class config:
        from_attributes=True

class UserResponse(BaseModel):
    id:int
    username:str
    email:str

    class config:
        from_attributes=True



