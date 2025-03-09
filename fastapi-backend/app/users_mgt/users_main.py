from fastapi import FastAPI
from loguru import logger

app = FastAPI()

from app.users_mgt import users, gifts

app.include_router(users.router, prefix="/user_mgt")
app.include_router(gifts.router, prefix="/user_mgt")