class Solution:

    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:

        ans = 0
        price = numExchange
        cur = numBottles
        while cur >= price:
            ans += 1
            cur -= price - 1
            price += 1

        return numBottles + ans
