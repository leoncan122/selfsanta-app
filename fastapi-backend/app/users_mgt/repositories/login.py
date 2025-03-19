

# from fastapi.responses import  HTTPException
from app.users_mgt.models.requests.users import Login

mock = [
    {
      "user_id": "ds1",
      "username": "user1",
      "email": "john@gmail.com",
      "password": "password1"
    },
    {
      "user_id": "ds2",
      "username": "user2",
      "email": "mark@gmail.com",
      "password": "password2"
    },
    {
      "user_id": "ds3",
      "username": "user3",
      "email": "peter@hotmail.com",
      "password": "password3"
    }
]


class LoginRepository:
    def __init__(self):
        self.data = mock
    
    def insert_login(self, user_credentials: Login) -> dict:
        try:
            self.data.append(user)
            return {"username": user.username, "password": user.password}
        except:
            return None
        
    def authenticate_user(self, user_id: str):
        try:
            user = self.data.get(id=user_id)
        
            return {
                    "user_id": "ds1",
                    "username": "user1",
                    "email": "user.email",
                    "gifts_registry": []

                }
        except:
            return None
        
    def update_password(self, user_id: str, new_password: str):
        try:
            user = self.data.get(id=user_id)
            user.update(new_password)
            return True
        except:
            return False