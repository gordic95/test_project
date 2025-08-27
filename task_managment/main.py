from fastapi import FastAPI, APIRouter
from .database import init_db
from .routers import register_tasks_router

init_db()

app = FastAPI()


app.include_router(register_tasks_router())
