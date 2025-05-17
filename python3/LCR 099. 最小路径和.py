class Solution:

    def minPathSum(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        dp[0][0] = grid[0][0]
        for idx in range(1, m):
            dp[idx][0] = dp[idx-1][0] + grid[idx][0]
        for idx in range(1, n):
            dp[0][idx] = dp[0][idx-1] + grid[0][idx]

        for idx in range(1, m):
            for jdx in range(1, n):
                dp[idx][jdx] = min(dp[idx-1][jdx], dp[idx][jdx-1]) + grid[idx][jdx]

        return dp[m-1][n-1]
