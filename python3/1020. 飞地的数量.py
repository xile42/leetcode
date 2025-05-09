class Solution:

    def numEnclaves(self, grid: List[List[int]]) -> int:

        ans = 0
        m, n = len(grid), len(grid[0])
        vis = [[False for _ in range(n)] for _ in range(m)]

        def dfs(i, j):

            vis[i][j] = True
            ans = 1
            valid = False
            for ii, jj in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                if 0 <= ii < m and 0 <= jj < n:
                    if grid[ii][jj] and not vis[ii][jj]:
                        res, _valid = dfs(ii, jj)
                        valid = valid | _valid
                        ans += res
                else:
                    valid = True

            return ans, valid

        for i in range(m):
            for j in range(n):
                if grid[i][j] and not vis[i][j]:
                    res, valid = dfs(i, j)
                    if not valid:
                        ans += res

        return ans
