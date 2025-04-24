class Solution:

    def uniquePaths(self, m: int, n: int) -> int:

        dp = [[0 for _ in range(n)] for _ in range(m)]
        for idx in range(m):
            dp[idx][0] = 1
        for idx in range(n):
            dp[0][idx] = 1

        for idx in range(1, m):
            for jdx in range(1, n):
                dp[idx][jdx] = dp[idx-1][jdx] + dp[idx][jdx-1]

        return dp[m-1][n-1]

