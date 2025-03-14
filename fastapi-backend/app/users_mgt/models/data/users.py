from pydantic import BaseModel
from datetime import datetime

class User(BaseModel):
    user_id: str
    username: str
    email: str
    password: str
    name: str
    created_at: datetime
    updated_at: datetime
    
