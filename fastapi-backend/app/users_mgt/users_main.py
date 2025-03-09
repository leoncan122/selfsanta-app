from fastapi import FastAPI
from loguru import logger

app = FastAPI()

from app.users_mgt.api import users, gifts

app.include_router(users.router, prefix="/users_mgt")
app.include_router(gifts.router, prefix="/users_mgt")