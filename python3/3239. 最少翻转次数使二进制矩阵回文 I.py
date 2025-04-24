class Solution:

    def minFlips(self, grid: List[List[int]]) -> int:

        cnt_r = cnt_c = 0
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n // 2):
                if grid[i][j] != grid[i][n - j - 1]:
                    cnt_r += 1

        for i in range(m // 2):
            for j in range(n):
                if grid[i][j] != grid[m - i - 1][j]:
                    cnt_c += 1

        return min(cnt_r, cnt_c)
