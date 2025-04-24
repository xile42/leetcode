class Solution:

    def maxMoves(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for j in range(1, n):
            for i in range(m):
                for ii, jj in (i - 1, j - 1), (i, j - 1), (i + 1, j - 1):
                    if 0 <= ii < m and 0 <= jj < n and grid[ii][jj] < grid[i][j] and (j == 1 or dp[ii][jj] != 0):
                        dp[i][j] = j
                        break

        return max(reduce(add, dp))
