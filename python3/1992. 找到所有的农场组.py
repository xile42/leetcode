class Solution:

    def findFarmland(self, grid: List[List[int]]) -> List[List[int]]:

        ans = list()
        m, n = len(grid), len(grid[0])
        vis = [[False for _ in range(n)] for _ in range(m)]

        def f(x, y):

            vis[x][y] = True
            mx_x, mx_y = x, y
            for xx, yy in (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1):
                if 0 <= xx < m and 0 <= yy < n and grid[xx][yy] == 1 and not vis[xx][yy]:
                    _x, _y = f(xx, yy)
                    mx_x = max(mx_x, _x)
                    mx_y = max(mx_y, _y)

            return mx_x, mx_y

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not vis[i][j]:
                    ii, jj = f(i, j)
                    ans.append([i, j, ii, jj])

        return ans
