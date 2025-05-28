# 网格图DFS模板
class Solution:

    def closedIsland(self, grid: List[List[int]]) -> int:

        ans = 0
        m, n = len(grid), len(grid[0])
        vis = [[False for _ in range(n)] for _ in range(m)]

        def dfs(i, j):

            vis[i][j] = True
            valid = True
            for ii, jj in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                if 0 <= ii < m and 0 <= jj < n:
                    if not grid[ii][jj] and not vis[ii][jj]:
                        _valid = dfs(ii, jj)
                        valid &= _valid
                else:
                    valid = False

            return valid

        for i in range(m):
            for j in range(n):
                if not grid[i][j] and not vis[i][j]:
                    ans += dfs(i, j)

        return ans
