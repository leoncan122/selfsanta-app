# from app.users_mgt.models.requests.users import UserAuthorizeReq
from app.users_mgt.repositories.users import Users_repo

class UsersService:
    def __init__(self):
        self.users_repo = Users_repo()
        
    def get_user(self, user_id: str):
        return self.users_repo.get_user(user_id)
    
    def authenticate_user(self, user):
        return self.users_repo.authenticate_user(user)
    
    def get_me(self):
        return self.users_repo.get_me()