from pydantic import BaseModel

class UserAuthorizeReq(BaseModel):
    username: str
    token: str
    
class Login(BaseModel):
    email: str
    password: str
    
class Signup(BaseModel):
    email: str
    password: str
    username: str
    name: str
    last_name: str
    birth_date: str
    phone: str
    address: str
    city: str
    state: str
    country: str

    