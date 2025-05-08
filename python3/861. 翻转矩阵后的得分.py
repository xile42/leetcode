class Solution:

    def matrixScore(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])

        def reverse_row(i):

            for j in range(n):
                grid[i][j] = 1 - grid[i][j]

        def reverse_col(j):

            for i in range(m):
                grid[i][j] = 1 - grid[i][j]

        for i in range(m):
            if grid[i][0] == 0:
                reverse_row(i)

        for j in range(n):
            c0 = c1 = 0
            for i in range(m):
                if grid[i][j]:
                    c1 += 1
                else:
                    c0 += 1
            if c1 < c0:
                reverse_col(j)

        ans = 0
        for i in range(m):
            ans += int("".join(map(str, grid[i])), 2)

        return ans
