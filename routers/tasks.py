from fastapi import APIRouter,Depends,HTTPException,status

from sqlalchemy.orm import Session

from database import get_db
from models import Task
from schemas import TaskCreate,TaskUpdate,TaskResponse

from security import get_current_user
import crud


router=APIRouter(prefix="/tasks",
                 tags=["Tasks"])

@router.post("",response_model=TaskResponse,status_code=status.HTTP_201_CREATED)
def create_task(task:TaskCreate,db:Session=Depends(get_db),current_user=Depends(get_current_user)):
    print("CURRENT USER:",current_user)
    new_task=Task(title=task.title,description=task.description,completed=task.completed,user_id=current_user)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

@router.get("",response_model=list[TaskResponse],status_code=status.HTTP_200_OK)
def get_tasks(skip:int=0,limit:int=10,db:Session=Depends(get_db),current_user=Depends(get_current_user)):
        print("CURRENT USER:",current_user)
        tasks=db.query(Task).filter(Task.user_id==current_user).offset(skip).limit(limit).all()
        return tasks

@router.get("/{task_id}",response_model=TaskResponse,status_code=status.HTTP_200_OK)
def get_task(task_id:int,db:Session=Depends(get_db),current_user:int=Depends(get_current_user)):
    existing_task=crud.get_task(db,task_id,current_user)
    if not existing_task:
        raise HTTPException(status_code=404,detail="Task no Found")
    return existing_task

@router.put("/{task_id}",response_model=TaskResponse,status_code=status.HTTP_200_OK)
def update_task(task_id:int,task:TaskUpdate,db:Session=Depends(get_db),current_user:int=Depends(get_current_user)):
    updated_task=crud.Update_task(db,
                                  task_id,
                                  current_user,
                                  task.title,
                                  task.description,
                                  task.completed)
    if not updated_task:
        raise HTTPException(status_code=404,detail="Task not found")
    
    return updated_task

@router.patch("/{task_id}",response_model=TaskResponse)
def patch_task(
               task_id:int,
               task:TaskUpdate,
               db:Session=Depends(get_db),
               current_user:int=Depends(get_current_user)):
    updates=task.model_dump(exclude_unset=True)
    updated_task=crud.patch_task(db,
                                task_id,
                                current_user,
                                updates)
    if not updated_task:
        raise HTTPException(status_code=404,detail="Task not found")
  
    return updated_task

@router.delete("/{task_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id:int,
                db:Session=Depends(get_db),
                current_user:int=Depends(get_current_user)):
    deleted_task=crud.delete_task(db,task_id,current_user)
    if not deleted_task:
        raise HTTPException(status_code=404,detail="Task not Found")
    return None