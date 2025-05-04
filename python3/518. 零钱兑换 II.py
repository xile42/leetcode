class Solution:

    def change(self, amount: int, coins: List[int]) -> int:

        @cache
        def f(cur, tar):

            if tar == 0:
                return 1

            if cur >= len(coins):
                return 0

            ans = 0
            for i in range(tar // coins[cur] + 1):
                ans += f(cur + 1, tar - i * coins[cur])

            return ans

        ans = f(0, amount)
        f.cache_clear()

        return ans
