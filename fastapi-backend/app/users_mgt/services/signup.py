
from app.users_mgt.repositories.signup import SignupRepository

class SignupService:
    def __init__(self):
        self.repo = SignupRepository()
        
    def create_signup(self, signup):
        self.repo.insert_signup(signup)
        return signup
    