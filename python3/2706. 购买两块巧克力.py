class Solution:

    def buyChoco(self, prices: List[int], money: int) -> int:

        cost = sum(sorted(prices)[:2])

        return money if money < cost else money - cost
