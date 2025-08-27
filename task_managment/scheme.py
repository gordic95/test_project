from datetime import datetime
from typing import Optional
from task_managment.models import StatusTask
from pydantic import BaseModel, ConfigDict


class TaskScheme(BaseModel):
    """Схема для задачи"""
    model_config = ConfigDict(from_attributes=True)

    id: str
    title: str
    description: Optional[str] = None
    status: StatusTask
    created_at: datetime



class TaskCreate(BaseModel):
    """Схема для создания задачи"""
    title: str
    description: Optional[str] = None


class TaskUpdate(BaseModel):
    """Схема для обновления задачи"""
    title: str
    description: Optional[str] = None
    status: Optional[StatusTask]
