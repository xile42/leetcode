class Solution:

    def countPathsWithXorValue(self, grid: List[List[int]], k: int) -> int:

        base = 10 ** 9 + 7
        m, n = len(grid), len(grid[0])
        cs = [[Counter() for _ in range(n)] for _ in range(m)]
        cs[0][0][grid[0][0]] += 1

        for i in range(1, n):
            for v in cs[0][i - 1]:
                cs[0][i][v ^ grid[0][i]] += 1
        for i in range(1, m):
            for v in cs[i - 1][0]:
                cs[i][0][v ^ grid[i][0]] += 1

        for i in range(1, m):
            for j in range(1, n):
                for v in cs[i - 1][j]:
                    cs[i][j][v ^ grid[i][j]] += cs[i - 1][j][v]
                    cs[i][j][v ^ grid[i][j]] %= base
                for v in cs[i][j - 1]:
                    cs[i][j][v ^ grid[i][j]] += cs[i][j - 1][v]
                    cs[i][j][v ^ grid[i][j]] %= base

        return cs[-1][-1][k] % base
