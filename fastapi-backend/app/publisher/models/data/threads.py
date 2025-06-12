from pydantic import BaseModel
from datetime import date
from .messages import Message
 
class Thread(BaseModel):
    id: str
    created_at: date
    messages: list[Message]  # List of message IDs