class Solution:

    def waysToStep(self, n: int) -> int:

        base = 10 ** 9 + 7
        dp = [1, 1, 2, 4]
        if n <= 3:
            return dp[n]

        while len(dp) < n + 1:
            dp.append((dp[-1] + dp[-2] + dp[-3]) % base)

        return dp[n] % base