from app.users_mgt.services.users import UsersService
from app.users_mgt.services.login import LoginService
from app.users_mgt.services.signup import SignupService
from app.users_mgt.services.funds import FundsService
from fastapi import Depends

def get_users_service(service=Depends(UsersService)):
    return service

def get_login_service(service=Depends(LoginService)):
    return service

def get_signup_service(service=Depends(SignupService)):
    return service

def get_funds_Service(service=Depends(FundsService)):
    return service