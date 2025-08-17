class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):

        self.n = n
        self.discount = discount
        self.products = products
        self.prices = prices
        self.count = 0
        self.product_price_map = dict(zip(products, prices))

    def getBill(self, product: List[int], amount: List[int]) -> float:

        total = 0
        for p, a in zip(product, amount):
            total += self.product_price_map[p] * a

        self.count += 1

        if self.count % self.n == 0:
            total -= (total * self.discount) / 100

        return total

# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)