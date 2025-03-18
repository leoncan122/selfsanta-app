
from app.celery.funds import create_fund_celery
from fastapi import APIRouter, Depends, HTTPException
from app.users_mgt.models.requests.funds import FundTransactionReq
from app.users_mgt.models.data.funds import FundTransaction

router = APIRouter()

@router.post("/funds")
async def insert_fund(transaction: FundTransactionReq):
    
    transaction_obj = FundTransaction(**transaction)
    
    try:
        create_fund_celery.delay()
        
        return {"message": "Create fund"}
    except HTTPException as e:
    
        return {"message": f"Error: ${e}"}
    
    
