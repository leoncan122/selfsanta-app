from pydantic import BaseModel
from datetime import datetime

class Gift(BaseModel):
    title: str
    price: str
    description: str
    url: str
    created_at: datetime
    updated_at: datetime
    
class GiftReq(BaseModel):
    title: str
    price: str
    description: str
    url: str
    
class GiftUpdateReq(BaseModel):
    title: str
    price: str
    description: str
    url: str

class GiftsRegistry(BaseModel):
    gifts: list[GiftReq]
    updated_at: datetime
