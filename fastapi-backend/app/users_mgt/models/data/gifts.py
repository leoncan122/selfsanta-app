from pydantic import BaseModel

class Gift(BaseModel):
    title: str
    price: str
    description: str
    url: str
