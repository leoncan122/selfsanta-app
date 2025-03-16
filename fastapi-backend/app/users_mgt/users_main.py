from fastapi import FastAPI
from loguru import logger

app = FastAPI()

from app.users_mgt.api import users, gifts, funds

app.include_router(users.router, prefix="/users")
app.include_router(gifts.router, prefix="/gifts")
app.include_router(funds.router, prefix="/funds")