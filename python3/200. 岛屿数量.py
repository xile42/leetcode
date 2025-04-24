class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        
        ans = 0
        m, n = len(grid), len(grid[0])
        vis = [[False for _ in range(n)] for _ in range(m)]

        def dfs(x, y):

            nonlocal vis
            vis[x][y] = True
            for xx, yy in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
                if 0 <= xx < m and 0 <= yy < n and grid[xx][yy] == "1" and not vis[xx][yy]:
                    dfs(xx, yy)

        for x in range(m):
            for y in range(n):
                if not vis[x][y] and grid[x][y] == "1":
                    ans += 1
                    dfs(x, y)

        return ans
