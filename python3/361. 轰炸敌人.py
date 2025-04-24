class Solution:

    def maxKilledEnemies(self, grid: List[List[str]]) -> int:

        m, n = len(grid), len(grid[0])

        row_pre = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            cnt = 0
            for j in range(n):
                if grid[i][j] == "W":
                    cnt = 0
                elif grid[i][j] == "E":
                    cnt += 1
                row_pre[i][j] = cnt

        row_suf = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            cnt = 0
            for j in range(n - 1, -1, -1):
                if grid[i][j] == "W":
                    cnt = 0
                elif grid[i][j] == "E":
                    cnt += 1
                row_suf[i][j] = cnt

        col_pre = [[0 for _ in range(n)] for _ in range(m)]
        for j in range(n):
            cnt = 0
            for i in range(m):
                if grid[i][j] == "W":
                    cnt = 0
                elif grid[i][j] == "E":
                    cnt += 1
                col_pre[i][j] = cnt

        col_suf = [[0 for _ in range(n)] for _ in range(m)]
        for j in range(n):
            cnt = 0
            for i in range(m - 1, -1, -1):
                if grid[i][j] == "W":
                    cnt = 0
                elif grid[i][j] == "E":
                    cnt += 1
                col_suf[i][j] = cnt

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "0":
                    ans = max(ans, row_pre[i][max(0, j - 1)] + row_suf[i][min(n - 1, j + 1)] + col_pre[max(0, i - 1)][j] + col_suf[min(m - 1, i + 1)][j])

        return ans
