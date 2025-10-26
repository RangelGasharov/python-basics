class Bank:

    def __init__(self, balance: list[int]):
        self.balance = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if len(self.balance) <= account1 - 1 or len(self.balance) <= account2 - 1:
            return False
        if self.balance[account1 - 1] >= money:
            self.balance[account1 - 1] -= money
            self.balance[account2 - 1] += money
            return True
        else:
            return False

    def deposit(self, account: int, money: int) -> bool:
        if len(self.balance) < account - 1:
            return False
        self.balance[account - 1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if len(self.balance) < account - 1:
            return False
        if self.balance[account - 1] >= money:
            self.balance[account - 1] -= money
            return True
        else:
            return False
