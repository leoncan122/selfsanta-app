from pydantic import BaseModel
from datetime import date

class FundTransactionReq(BaseModel):
    amount: float
    sender_id: str
    beneficary_id: str
    description: str
    created_at: date