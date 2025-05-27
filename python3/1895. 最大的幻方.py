class Solution:

    def largestMagicSquare(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        rows = [[0] * (n + 2) for _ in range(m + 2)]
        cols = [[0] * (n + 2) for _ in range(m + 2)]
        dias = [[0] * (n + 2) for _ in range(m + 2)]
        ants = [[0] * (n + 2) for _ in range(m + 2)]

        #预处理前缀和：行、列、斜、反斜
        for i, row in enumerate(grid, start=1):
            for j, v in enumerate(row, start=1):
                rows[i][j] = rows[i][j - 1] + v
                cols[i][j] = cols[i - 1][j] + v
                dias[i][j] = dias[i - 1][j - 1] + v
                ants[i][j] = ants[i - 1][j + 1] + v

        def check(k, i, j):

            s = dias[i][j] - dias[i - k][j - k]
            if ants[i][j - k + 1] - ants[i - k][j + 1] != s:
                return False
            for r in range(i - k + 1,i + 1):
                if rows[r][j] - rows[r][j - k] != s:
                    return False
            for c in range(j - k + 1,j + 1):
                if cols[i][c] - cols[i - k][c] != s:
                    return False

            return True

        #暴力枚举：边长、矩形右下角坐标+暴力检查check(k,i,j)
        for k in range(min(n, m), 1, -1):
            for i in range(k, m + 1):
                for j in range(k, n + 1):
                    if check(k, i, j):
                        return k

        return 1
