from fastapi import APIRouter, Depends, HTTPException
from loguru import logger
from fastapi.responses import JSONResponse

from app.users_mgt.models.requests.gifts import GiftReq
from app.users_mgt.models.data.gifts import Gift

router = APIRouter()

