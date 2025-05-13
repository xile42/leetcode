class Solution:

    def maxSum(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        ans = 0
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                ans = max(ans, grid[i][j] + grid[i - 1][j] + grid[i - 1][j - 1] + grid[i - 1][j + 1] + grid[i + 1][j] + grid[i + 1][j - 1] + grid[i + 1][j + 1])

        return ans
