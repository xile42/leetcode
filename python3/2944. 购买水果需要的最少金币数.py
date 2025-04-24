class Solution:

    def minimumCoins(self, prices: List[int]) -> int:

        n = len(prices)

        @cache
        def f(cur, buy):

            if cur > n:
                return 0

            ans = inf
            if cur <= buy:
                ans1 = prices[cur - 1] + f(cur + 1, max(buy, cur * 2))
                ans2 = f(cur + 1, buy)
                ans = min(ans, ans1, ans2)
            else:
                ans1 = prices[cur - 1] + f(cur + 1, max(buy, cur * 2))
                ans = min(ans, ans1)

            return ans

        ans = f(1, -1)

        return ans
