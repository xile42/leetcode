class Solution:

    def countPaths(self, grid: List[List[int]]) -> int:

        base = 10 ** 9 + 7
        m, n = len(grid), len(grid[0])

        @cache
        def f(i, j):
            
            ans = 1
            for ii, jj in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                if 0 <= ii < m and 0 <= jj < n and grid[i][j] < grid[ii][jj]:
                    ans += f(ii, jj)

            return ans % base

        return sum([f(i, j) for i in range(m) for j in range(n)]) % base
