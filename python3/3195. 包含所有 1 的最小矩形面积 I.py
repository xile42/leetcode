class Solution:

    def minimumArea(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        x, y = inf, inf
        xx, yy = -inf, -inf
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    x = min(x, i)
                    y = min(y, j)
                    xx = max(xx, i)
                    yy = max(yy, j)

        return (xx - x + 1) * (yy - y + 1)
