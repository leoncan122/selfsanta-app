
mock = [
    {
        "id": "1",
        "username": "user1",
        "password": "password1",
        "email": "",
    },
    {
        "id": "2",
        "username": "user2",
        "password": "password2",
        "email": "",
    },
    {
        "id": "3",
        "username": "user3",
        "password": "password3",
        "email": "",
    },        
]



class UsersRepository():
    def __init__(self):
        self.data = mock
    
    def get_user(self, user_id: str):
        try:
            
            user = self.data.get(id=user_id)
            
            return {
                "id": "user.id",
                "username": "user.username",
                "gifts_registry": []
            }
        except:
            return None
    
    def create_user(self, user):
        try:
            self.data.append(user)
            return user
        except:
            return None
        
    def update_user(self, user_id: str, user):
        try:
            user = self.data.get(id=user_id)
            user.update(user)
            return user
        except:
            return None
    
    def authorize_user(self, user_id: str):
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
        
    
        
        