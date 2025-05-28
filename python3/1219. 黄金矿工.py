class Solution:

    def getMaximumGold(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        vis = [[False for _ in range(n)] for _ in range(m)]
        ans = 0

        def f(x, y):

            ans = 0
            vis[x][y] = True
            for xx, yy in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
                if 0 <= xx < m and 0 <= yy < n and not vis[xx][yy] and grid[x][y]:
                    ans = max(ans, f(xx, yy))
            vis[x][y] = False

            return ans + grid[x][y]

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    ans = max(ans, f(i, j))

        return ans
