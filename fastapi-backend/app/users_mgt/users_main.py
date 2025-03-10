from fastapi import FastAPI
from loguru import logger

app = FastAPI()

from app.users_mgt.api import users, gifts

app.include_router(users.router, prefix="/users")
app.include_router(gifts.router, prefix="/gifts")