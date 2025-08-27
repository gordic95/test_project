import uuid
from datetime import datetime, timezone
from .database import Base
from enum import Enum
from sqlalchemy import Enum as SQLEnum, DateTime, String
from sqlalchemy.orm import Mapped, mapped_column

class StatusTask(Enum):
    """Статус задачи"""
    created = "created"
    in_progress = "in_progress"
    completed = "completed"

class Task(Base):
    """Модель задачи"""
    __tablename__ = "tasks"

    id : Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    title : Mapped[str] = mapped_column(String(255), nullable=False)
    description : Mapped[str] = mapped_column(String(255), nullable=True)
    status : Mapped[StatusTask] = mapped_column(SQLEnum(StatusTask), default=StatusTask.created)
    created_at : Mapped[datetime] = mapped_column(DateTime, default=datetime.now(timezone.utc))


