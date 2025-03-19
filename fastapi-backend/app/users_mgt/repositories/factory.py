from app.users_mgt.repositories.users import UsersRepository
from app.users_mgt.repositories.login import LoginRepository
from app.users_mgt.repositories.signup import SignupRepository
from app.users_mgt.repositories.funds import FundsRepository
from fastapi import Depends


def get_users_repo(repo=Depends(UsersRepository)):
    return repo

def get_login_repo(repo=Depends(LoginRepository)):
    return repo

def get_signup_repo(repo=Depends(SignupRepository)):
    return repo

def get_funds_repo(repo=Depends(FundsRepository)):
    return repo

