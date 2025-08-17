class ProductOfNumbers:

    def __init__(self):

        self.prod = list()
        self.prod.append(1)
        self.last_zero = -inf

    def add(self, num: int) -> None:

        self.prod.append((self.prod[-1] * num) if num != 0 else 1)
        if num == 0:
            self.last_zero = len(self.prod) - 1

    def getProduct(self, k: int) -> int:

        if self.last_zero >= len(self.prod) - k:
            return 0

        return self.prod[-1] // self.prod[-k - 1]

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)