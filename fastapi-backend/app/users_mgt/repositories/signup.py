from typing import List
from pydantic import BaseModel



class Signup(BaseModel):
    sign_id: int
    stud_id: int
    username: str
    password: str

def mock_signups() -> List[Signup]:
    return [
        Signup(sign_id=1, stud_id=101, username="user1", password="pass1"),
        Signup(sign_id=2, stud_id=102, username="user2", password="pass2"),
        Signup(sign_id=3, stud_id=103, username="user3", password="pass3"),
    ]

class SignupRepository:
    def __init__(self):
        self.data = mock_signups()
        
    def create_signup(self, signup: Signup) -> Signup:
        try:
            self.data.append(signup)
            return signup    
        except:
            return None
        
    def get_signup(self, sign_id: str) -> Signup:
        try:
            signup = self.data.get(id=sign_id)
            return signup
        except:
            return None    
    
    def delete_signup(self, sign_id: str) -> bool:
        try:
            signup = self.data.get(id=sign_id)
            self.data.remove(signup)
            return True
        except:
            return False
        