from pydantic import BaseModel
from datetime import date

class Gift(BaseModel):
    title: str
    price: str
    description: str
    url: str
    created_at: date
    updated_at: date
    
class GiftsRegistry(BaseModel):
    user_id: str
    gifts: list[Gift]
    updated_at: date