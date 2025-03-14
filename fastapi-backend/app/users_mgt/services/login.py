
from app.users_mgt.repositories.login import LoginRepository

class LoginService:
    def __init__(self):
        self.repo = LoginRepository()
        
    def create_login(self, login):
        login = self.repo.insert_login(login)
        return login
    
    def update_login_password(self, user_id, new_password):
        login = self.repo.update_password(user_id, new_password)
        return login
    