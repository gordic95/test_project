from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import get_db
from .models import Task
from .scheme import TaskScheme, TaskCreate, TaskUpdate

def register_tasks_router(db: Session = Depends()):
    routers = APIRouter(prefix="/tasks", tags=["tasks"])

    @routers.post("/create_task", response_model=TaskScheme)
    def create_task(task_data: TaskCreate, db: Session = Depends(get_db)):
        """Метод для создания задачи"""
        task = Task(**task_data.model_dump())
        db.add(task)
        db.commit()
        db.refresh(task)
        return task

    @routers.get("/get_task/{task_id}", response_model=TaskScheme)
    def get_task(task_id: str, db: Session = Depends(get_db)):
        """Метод для получения задачи по uuid"""
        task = db.query(Task).filter(Task.id == task_id).first()
        if not task:
            raise HTTPException(
                status_code=404,
                detail=f"Task with id {task_id} not found"
            )
        return task


    @routers.get("/get_list")
    def get_list_task(db: Session = Depends(get_db)):
        """Метод для получения списка задач"""
        task = db.query(Task).all()
        return task

    @routers.put("/update_task/{task_id}", response_model=TaskScheme)
    def update_task(task_id: str, task_data: TaskUpdate, db: Session = Depends(get_db)):
        """Метод для обновления задачи"""
        task = db.query(Task).filter(Task.id == task_id).first()
        if not task:
            raise HTTPException(
                status_code=404,
                detail=f"Task with id {task_id} not found"
            )
        else:
            task.title = task_data.title
            task.description = task_data.description
            task.status = task_data.status
            db.commit()
            db.refresh(task)
            return  task

    @routers.delete("/delete_task/{task_id}")
    def delete_task(task_id: str, db: Session = Depends(get_db)):
        """Метод для удаления задачи"""
        task = db.query(Task).filter(Task.id == task_id).first()
        if not task:
            raise HTTPException(
                status_code=404,
                detail=f"Task with id {task_id} not found"
            )
        else:
            db.delete(task)
            db.commit()
            return {"message": f"Task with id {task_id} deleted"}

    return routers


