class Solution:

    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)

        @cache
        def f(i, s, c):

            if c == 0 and s == 0:
                return 0

            if i == n - 1:
                return 0 if s == 0 else prices[i]

            ans = list()
            ans.append(f(i + 1, s, c))
            if s == 1:
                ans.append(f(i + 1, 1 - s, c) + prices[i])
            elif c > 0:
                ans.append(f(i + 1, 1 - s, c - 1) - prices[i])

            return max(ans)

        return f(0, 0, 2)
