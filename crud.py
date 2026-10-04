from sqlalchemy.orm import Session
from models import User,Task
from schemas import TaskCreate,TaskUpdate,TaskPatch
import crud



def get_user_by_email(db:Session,email:str):
    return db.query(User).filter(User.email==email).first()

def get_user_by_username(db:Session,username:str):
    return db.query(User).filter(User.username==username).first()

def create_user(db:Session,username:str,email:str,password:str):
    new_user=User(username=username,
                  email=email,
                  password=password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def create_task(db:Session,
                title:str,
                description:bool,
                completed:bool,
                user_id:int):
    new_task=Task(title=title,
                  description=description,
                  completed=completed,
                  user_id=user_id)
    
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

def get_tasks(db:Session,
              user_id:int,
              skip:int=0,
              limit:int=10):
    return (db.query(Task)
            .filter(Task.user_id==user_id)
            .offset(skip).
            limit(limit)
            .all())

def get_task(db:Session,
            task_id:int,
            user_id:int):
    return (db.query(Task).filter(Task.id==task_id,Task.user_id==user_id).first())

def Update_task(db:Session,
                task_id:int,
                user_id:int,
                title:str,
                description:str,
                completed:bool):
        task=db.query(Task).filter(Task.id==task_id,Task.user_id==user_id).first()
        if  not task :
            return None
        task.title=title
        task.description=description
        task.completed=completed
        db.commit()
        db.refresh(task)
        return task

def patch_task(db:Session,
               task_id:int,
               user_id:int,
               updates:dict):
    task=db.query(Task).filter(Task.id==task_id,Task.user_id==user_id).first()
    if not task:
        return None

    for field,value in updates.items():
        setattr(task,field,value)
    db.commit()
    db.refresh(task)
    return task

def delete_task(db:Session,task_id:int,user_id:int):
    existing_task=db.query(Task).filter(Task.id==task_id,Task.user_id==user_id).first()
    if existing_task is None:
        return None
    db.delete(existing_task)
    db.commit()
    return existing_task