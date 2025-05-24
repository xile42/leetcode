class Solution:

    def findMaxFish(self, grid: List[List[int]]) -> int:

        ans = 0
        m, n = len(grid), len(grid[0])
        vis = [[False for _ in range(n)] for _ in range(m)]

        def f(i, j):
            vis[i][j] = True
            ans = grid[i][j]
            for ii, jj in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                if 0 <= ii < m and 0 <= jj < n and grid[ii][jj] and not vis[ii][jj]:
                    ans += f(ii, jj)
            return ans

        for i in range(m):
            for j in range(n):
                if grid[i][j] and not vis[i][j]:
                    ans = max(ans, f(i, j))

        return ans
