class StockSpanner:

    def __init__(self):

        self.st = [[-1, inf]]
        self.day = -1

    def next(self, price: int) -> int:

        while self.st[-1][-1] <= price:
            self.st.pop(-1)
        self.day += 1
        ans = self.day - self.st[-1][0]
        self.st.append([self.day, price])

        return ans

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)