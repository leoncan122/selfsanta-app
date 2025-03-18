
from app.users_mgt.models.data.funds import Fund

mock = [
    Fund(
        trans_id="1",
        amount=100,
        sender_id="user1",
        beneficary_id="user2",
        description="Gift",
        created_at="2021-01-01"
    ),
    Fund(
        trans_id="2",
        amount=200,
        sender_id="user2",
        beneficary_id="user3",
        description="Gift",
        created_at="2021-01-02"
    )
]

class FundsRepository:
    def __init__(self):
        self.data = mock
    
    def create_fund(self, fund):
        try:
            self.data.append(fund)
            return fund
        except:
            return None
    
    def get_fund(self, fund_id: str):
        try:
            fund = self.data.get(id=fund_id)
            return fund
        except:
            return None
    def get_funds_registry(self, user_id: str):
        try:
            funds = self.data.get(sender_id=user_id)
            return funds
        except:
            return None