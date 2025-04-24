class Solution:

    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)

        @cache
        def f(i, s):

            if i == n - 1:
                return 0 if s == 0 else prices[i]

            return max(f(i + 1, s), f(i + 1, 1 - s) + prices[i] * (1 if s == 1 else -1))

        return f(0, 0)
