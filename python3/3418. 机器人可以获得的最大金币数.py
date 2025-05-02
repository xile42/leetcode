class Solution:

    def maximumAmount(self, coins: List[List[int]]) -> int:

        m, n = len(coins), len(coins[0])
        dp = [[[-inf for _ in range(4)] for _ in range(n)] for _ in range(m)]

        if coins[0][0] >= 0:
            dp[0][0][2] = coins[0][0]
        else:
            dp[0][0][2] = coins[0][0]
            dp[0][0][1] = 0

        for i in range(1, n):
            if coins[0][i] >= 0:
                for k in range(3):
                    dp[0][i][k] = dp[0][i - 1][k] + coins[0][i]
            else:
                # dp[0][i][2] = dp[0][i - 1][2] + coins[0][i]
                for k in range(3):
                    dp[0][i][k] = max(dp[0][i - 1][k] + coins[0][i], dp[0][i - 1][k + 1])

        for i in range(1, m):
            if coins[i][0] >= 0:
                for k in range(3):
                    dp[i][0][k] = dp[i - 1][0][k] + coins[i][0]
            else:
                # dp[i][0][2] = dp[i - 1][0][2] + coins[i][0]
                for k in range(3):
                    dp[i][0][k] = max(dp[i - 1][0][k] + coins[i][0], dp[i - 1][0][k + 1])

        for i in range(1, m):
            for j in range(1, n):
                for k in range(2, -1, -1):
                    if coins[i][j] >= 0:
                        dp[i][j][k] = max(dp[i - 1][j][k], dp[i][j - 1][k]) + coins[i][j]
                    else:
                        dp[i][j][k] = max(max(dp[i - 1][j][k], dp[i][j - 1][k]) + coins[i][j], max(dp[i - 1][j][k + 1], dp[i][j - 1][k + 1]))

        return max(dp[-1][-1][:3])
