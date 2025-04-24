class Solution:

    def differenceOfDistinctValues(self, grid: List[List[int]]) -> List[List[int]]:

        m, n = len(grid), len(grid[0])
        ans = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                s = set()
                ii, jj = i - 1, j - 1
                while ii >= 0 and jj >= 0:
                    s.add(grid[ii][jj])
                    ii -= 1
                    jj -= 1
                a = len(s)
                s = set()
                ii, jj = i + 1, j + 1
                while ii < m and jj < n:
                    s.add(grid[ii][jj])
                    ii += 1
                    jj += 1
                b = len(s)
                ans[i][j] = abs(a - b)

        return ans
