# 网格图DFS模板
class Solution:

    def pacificAtlantic(self, grid: List[List[int]]) -> List[List[int]]:

        m, n = len(grid), len(grid[0])
        mark = [[0 for _ in range(n)] for _ in range(m)]

        def dfs(i, j):

            vis[i][j] = True
            mark[i][j] += 1
            for ii, jj in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                if 0 <= ii < m and 0 <= jj < n and grid[ii][jj] >= grid[i][j] and not vis[ii][jj]:
                    dfs(ii, jj)

        vis = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            if not vis[i][0]:
                dfs(i, 0)
        for j in range(1, n):
            if not vis[0][j]:
                dfs(0, j)

        vis = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            if not vis[i][n - 1]:
                dfs(i, n - 1)
        for j in range(n - 1):
            if not vis[m - 1][j]:
                dfs(m - 1, j)

        ans = [[i, j] for i in range(m) for j in range(n) if mark[i][j] == 2]

        return ans
