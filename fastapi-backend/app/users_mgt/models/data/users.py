from pydantic import BaseModel
from datetime import date

class User(BaseModel):
    user_id: str
    username: str
    email: str
    password: str
    name: str
    created_at: date
    updated_at: date
    
    
class UserLogin(BaseModel):
    user_id: str
    username: str
    password: str
    email: str
    