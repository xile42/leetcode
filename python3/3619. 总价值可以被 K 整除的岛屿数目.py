class Solution:

    def countIslands(self, grid: List[List[int]], k: int) -> int:

        ans = 0
        m, n = len(grid), len(grid[0])
        vis = [[False for _ in range(n)] for _ in range(m)]

        def f(i, j):

            vis[i][j] = True
            res = grid[i][j]
            for ii, jj in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                if 0 <= ii < m and 0 <= jj < n and grid[ii][jj] != 0 and not vis[ii][jj]:
                    res += f(ii, jj)

            return res

        for i in range(m):
            for j in range(n):
                if not vis[i][j] and grid[i][j] != 0:
                    v = f(i, j)
                    if v % k == 0:
                        ans += 1

        return ans
