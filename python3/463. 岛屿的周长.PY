class Solution:

    def islandPerimeter(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])

        def f(i, j):

            if not (0 <= i < m and 0 <= j < n):
                return 0

            return grid[i][j]

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    ans += 4 - f(i + 1, j) - f(i - 1, j) - f(i, j + 1) - f(i, j - 1)

        return ans
