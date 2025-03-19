
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from loguru import logger
from fastapi.responses import JSONResponse

class UserAuthenticationReq(BaseModel):
    username: str
    password: str
    
class UserSignupReq(BaseModel):
    username: str
    email: str
    password: str
    name: str

router = APIRouter()

@router.get("/{user_id}")
async def get_user(user_id: str):
    return {"user_id": user_id}

@router.post("/login")
async def authenticate_user(user: UserAuthenticationReq):
    try:
        #logica para autenticar al usuario
        return {"username": user.username, "password": user.password}
    except Exception as e:
        logger.error(f"Error al autenticar al usuario: {e}")
        return JSONResponse(status_code=500, content={"message": "Internal server error"})

@router.post("/signup")
async def signup_user(user: UserSignupReq):
    try:
        #logica para registrar al usuario
        return {"username": user.username, "password": user.password, "name": user.name}
    except Exception as e:
        logger.error(f"Error al registrar al usuario: {e}")
        return JSONResponse(status_code=500, content={"message": "Internal server error"})

@router.get("/me/{user_id}")
async def get_me():
    try:
        #logica para obtner el usuario actual
        return {"username": "sindinero23", "password": "mkfnsd8s", "name": "Juan Perez"}
    except Exception as e:
        logger.error(f"Error al obtener el usuario {e}")
        return JSONResponse(status_code=500, content={ "msg": "Internal server error" })
    
    
# UPDATE USER

# DELETE USER



