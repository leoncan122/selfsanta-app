from pydantic import BaseModel
from datetime import datetime

class Gift(BaseModel):
    title: str
    price: str
    description: str
    url: str
    created_at: datetime
    updated_at: datetime
    
class GiftsRegistry(BaseModel):
    gifts: list[Gift]
    updated_at: datetime