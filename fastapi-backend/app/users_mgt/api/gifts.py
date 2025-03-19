from fastapi import APIRouter, Depends, HTTPException
from loguru import logger
from fastapi.responses import JSONResponse

from app.users_mgt.models.requests.gifts import GiftReq
from app.users_mgt.models.data.gifts import Gift

router = APIRouter()

@router.get("/{gift_id}")
def get_gift(gift_id: str) -> Gift:
    return {"gift_id": gift_id}

@router.post("/")
async def add_gift(gift: GiftReq):
    try:
        # Lógica para agregar el regalo
        return {"title": gift.title, "price": gift.price, "description": gift.description, "link": gift.url}
    except Exception as e:
        logger.error(f"Error al agregar el regalo: {e}")
        return JSONResponse(status_code=500, content={"message": "Internal server error"})
    
@router.put("/{gift_id}")
async def update_gift(gift_id: str, gift: GiftReq) -> Gift:
    try:
        #actualizar el regalo
        return { "msg": f"Regalo {gift_id} actualizado correctamente" }
    except Exception as e:
        logger.error(f"Error al actualizar el regalo: {e}")
        return JSONResponse(status_code=500, content={"message": "Internal server error"})
    
@router.delete("/{gift_id}")
async def delete_gift(gift_id: str) -> dict:
    try:
        #eliminar el regalo
        return { "msg": f"Regalo {gift_id} eliminado correctamente" }
    except Exception as e:
        logger.error(f"Error al eliminar el regalo: {e}")
        return JSONResponse(status_code=500, content={"message": "Internal server error"})

