from pydantic import BaseModel
from datetime import date

class Message(BaseModel):
    id: str
    from_: str
    to: str
    body: str
    timestamp: date
    thread_id: str
    isRead: bool