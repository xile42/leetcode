class Solution:

    def waysToChange(self, n: int) -> int:

        base = 10 ** 9 + 7
        vs = [25, 10, 5, 1]
        dp = [0] * (n + 1)
        dp[0] = 1

        for v in vs[::-1]:
            for i in range(v, n + 1):
                dp[i] += dp[i - v]
                dp[i] %= base

        return dp[-1] % base
