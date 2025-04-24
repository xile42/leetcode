class Solution:

    def minFallingPathSum(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        dp = [[inf for _ in range(n)] for _ in range(m)]

        for i in range(n):
            dp[0][i] = grid[0][i]

        for i in range(1, m):
            for j in range(n):
                row = dp[i - 1].copy()
                row.pop(j)
                dp[i][j] = min(row) + grid[i][j]

        return min(dp[-1])
