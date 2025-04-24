class Solution:

    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(n):
            dp[0][i] = grid[0][i]

        for i in range(1, m):
            for j in range(n):
                values = list()
                for k in range(n):
                    values.append(dp[i - 1][k] + moveCost[grid[i - 1][k]][j])
                dp[i][j] = min(values) + grid[i][j]

        return min(dp[-1])
