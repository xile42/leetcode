class Solution:

    def maxScore(self, grid: List[List[int]]) -> int:

        ans = -inf
        m, n = len(grid), len(grid[0])
        f = [[inf] * (n + 1) for _ in range(m + 1)]
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                mn = min(f[i + 1][j], f[i][j + 1])
                ans = max(ans, x - mn)
                f[i + 1][j + 1] = min(mn, x)

        return ans
