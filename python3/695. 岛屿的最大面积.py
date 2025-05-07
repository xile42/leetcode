class Solution:

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        ans = 0
        m, n = len(grid), len(grid[0])
        vis = [[False for _ in range(n)] for _ in range(m)]

        def dfs(i, j):

            vis[i][j] = True
            ans = 1
            for ii, jj in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                if 0 <= ii < m and 0 <= jj < n and grid[ii][jj] and not vis[ii][jj]:
                    ans += dfs(ii, jj)

            return ans

        for i in range(m):
            for j in range(n):
                if grid[i][j] and not vis[i][j]:
                    ans = max(ans, dfs(i, j))

        return ans

