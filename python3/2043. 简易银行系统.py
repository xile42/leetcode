class Bank:

    def __init__(self, balance: List[int]):

        self.d = {i: v for i, v in enumerate(balance)}
        self.n = len(self.d)

    def transfer(self, account1: int, account2: int, money: int) -> bool:

        if not (1 <= account1 <= self.n and 1 <= account2 <= self.n and self.d[account1 - 1] >= money):
            return False

        self.d[account1 - 1] -= money
        self.d[account2 - 1] += money

        return True

    def deposit(self, account: int, money: int) -> bool:

        if not (1 <= account <= self.n):
            return False

        self.d[account - 1] += money

        return True

    def withdraw(self, account: int, money: int) -> bool:

        if not (1 <= account <= self.n and self.d[account - 1] >= money):
            return False

        self.d[account - 1] -= money

        return True

# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)