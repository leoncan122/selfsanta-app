from pydantic import BaseModel
from datetime import date

class FundTransaction(BaseModel):
    trans_id: str
    amount: float
    sender_id: str
    beneficary_id: str
    description: str
    created_at: str

class Fund(BaseModel):
    trans_id: str
    amount: float
    sender_id: str
    beneficary_id: str
    description: str
    created_at: str
    
class FundRegistry(BaseModel):
    user_id: str
    funds: list[Fund]
    updated_at: date

