class Solution:

    def countHousePlacements(self, n: int) -> int:

        base = pow(10, 9) + 7
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n + 1):
            dp[i] = (dp[i-1] + dp[i-2]) % base

        return (dp[-1] ** 2) % base
