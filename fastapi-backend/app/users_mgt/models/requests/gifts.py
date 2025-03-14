from pydantic import BaseModel
from datetime import datetime

    
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


