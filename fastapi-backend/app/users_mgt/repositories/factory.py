from app.users_mgt.repositories.users import Users_repo
from app.users_mgt.repositories.login import LoginRepository
from app.users_mgt.repositories.signup import SignupRepository
from fastapi import Depends


def get_users_repo(repo=Depends(Users_repo)):
    return repo

def get_login_repo(repo=Depends(LoginRepository)):
    return repo

def get_signup_repo(repo=Depends(SignupRepository)):
    return repo