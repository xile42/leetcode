class Solution:

    def largestArea(self, grid: List[str]) -> int:

        ans = 0
        m, n = len(grid), len(grid[0])
        vis = [[False for _ in range(n)] for _ in range(m)]

        def f(i, j):
            vis[i][j] = True
            tar = grid[i][j]
            valid = True
            ans = 1
            for ii, jj in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                if 0 <= ii < m and 0 <= jj < n:
                    if grid[ii][jj] == "0":
                        valid = False
                    if grid[ii][jj] == tar and not vis[ii][jj]:
                        res, _valid = f(ii, jj)
                        ans += res
                        valid = valid & _valid
                else:
                    valid = False
            return ans, valid

        for i in range(m):
            for j in range(n):
                if grid[i][j] != "0" and not vis[i][j]:
                    res, valid = f(i, j)
                    if valid:
                        ans = max(ans, res)

        return ans
