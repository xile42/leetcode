class ATM:

    def __init__(self):

        self.cnt = Counter()        
        self.values = [20, 50, 100, 200, 500]

    def deposit(self, banknotesCount: List[int]) -> None:

        for i, n in enumerate(banknotesCount):
            value = self.values[i]
            self.cnt[value] += n
            
    def withdraw(self, amount: int) -> List[int]:

        cnt = self.cnt.copy()
        ans = [0] * 5
        for i, v in enumerate(self.values[::-1]):
            n = min(cnt[v], amount // v)
            amount -= v * n
            cnt[v] -= n
            ans[i] += n

        if amount:
            return [-1]

        self.cnt = cnt
        return ans[::-1]
                


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)
