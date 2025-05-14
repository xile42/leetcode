class Solution:

    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:

        return 100 - int(purchaseAmount / 10 + 0.5) * 10