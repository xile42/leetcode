class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:

        coins = sorted(coins, reverse=True)

        @cache
        def f(x):

            if x == 0:
                return 0
            elif x < 0:
                return inf

            ans = inf
            for coin in coins:
                need = 1 + f(x - coin)
                ans = min(ans, need)

            return ans

        ans = f(amount)
        return ans if ans < inf else -1
