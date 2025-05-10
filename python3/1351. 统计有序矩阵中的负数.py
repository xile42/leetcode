class Solution:

    def countNegatives(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                ans += grid[i][j] < 0

        return ans
