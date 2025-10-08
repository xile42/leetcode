class Solution:

    def minimumLines(self, stockPrices: List[List[int]]) -> int:

        n = len(stockPrices)
        ans = 0
        cur = (inf, inf)
        stockPrices.sort()

        for i in range(1, n):
            x1, y1 = stockPrices[i - 1]
            x2, y2 = stockPrices[i]
            a, b = y2 - y1, x2 - x1
            g = gcd(a, b)
            k = (a // g, b // g)
            if k != cur:
                ans += 1
                cur = k

        return ans
