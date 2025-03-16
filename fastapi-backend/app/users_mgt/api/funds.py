
from app.celery.funds import create_fund_celery
from fastapi import APIRouter, Depends, HTTPException

router = APIRouter()

@router.get("/funds")
async def insert_fund():
    try:
        create_fund_celery.delay()
        
        return {"message": "Create fund"}
    except HTTPException as e:
    
        return {"message": f"Error: ${e}"}