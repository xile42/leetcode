class Solution:

    def maxProductPath(self, grid: List[List[int]]) -> int:

        base = pow(10, 9) + 7
        m, n = len(grid), len(grid[0])
        mx = [[-inf for _ in range(n)] for _ in range(m)]
        mn = [[inf for _ in range(n)] for _ in range(m)]

        mx[0][0] = mn[0][0] = grid[0][0]
        for i in range(1, n):
            values = [mx[0][i - 1] * grid[0][i], mn[0][i - 1] * grid[0][i]]
            mx[0][i] = max(values)
            mn[0][i] = min(values)
        for i in range(1, m):
            values = [mx[i - 1][0] * grid[i][0], mn[i - 1][0] * grid[i][0]]
            mx[i][0] = max(values)
            mn[i][0] = min(values)

        for i in range(1, m):
            for j in range(1, n):
                values = [mx[i - 1][j] * grid[i][j], mx[i][j - 1] * grid[i][j], mn[i - 1][j] * grid[i][j], mn[i][j - 1] * grid[i][j]]
                mx[i][j] = max(values)
                mn[i][j] = min(values)

        ans = mx[-1][-1]

        return -1 if ans < 0 else ans % base
