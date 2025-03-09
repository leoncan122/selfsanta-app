from fastapi import APIRouter, Depends, HTTPException
from loguru import logger
from fastapi.responses import JSONResponse
from app.users_mgt.models.requests import GiftReq
router = APIRouter()

@router.get("/gifts/{gift_id}")
def get_gift(gift_id: str):
    return {"gift_id": gift_id}

@router.post("/gifts")
async def add_gift(gift: GiftReq):
    try:
        # Lógica para agregar el regalo
        return {"title": gift.title, "price": gift.price, "description": gift.description, "link": gift.url}
    except Exception as e:
        logger.error(f"Error al agregar el regalo: {e}")
        return JSONResponse(status_code=500, content={"message": "Internal server error"})
    
@router.put("/gifts/{gift_id}")
async def update_gift(gift_id: str, gift: GiftReq):
    try:
        #actualizar el regalo
        return { msg: f"Regalo {gift_id} actualizado correctamente" }
    except Exception as e:
        logger.error(f"Error al actualizar el regalo: {e}")
        return JSONResponse(status_code=500, content={"message": "Internal server error"})
