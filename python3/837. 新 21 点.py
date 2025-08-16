class Solution:

    def new21Game(self, n: int, k: int, maxPts: int) -> float:

        dp = [0] * (k + maxPts)
        for i in range(k, k + maxPts):
            dp[i] = 1.0 if i <= n else 0.0
        s = sum(dp[k:k + maxPts])
        for i in range(k - 1, -1, -1):
            dp[i] = s / maxPts
            s -= dp[i + maxPts]
            s += dp[i]

        return dp[0]
