from app.users_mgt.repositories.funds import FundsRepository

class FundsService:
    def __init__(self):
        self.repo = FundsRepository()
        
    def get_fund(self, fund_id):
        fund = self.repo.get_fund(fund_id)
        return fund
    
    def insert_fund(self, fund):
        fund_saved = self.repo.create_fund(fund)
        return fund_saved
    
    def get_funds_registry(self, user_id):
        funds = self.repo.get_funds_registry(user_id)
        return funds