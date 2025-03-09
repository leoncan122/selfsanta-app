from pydantic import BaseModel

class GiftReq(BaseModel):
    title: str
    price: str
    description: str
    url: str
