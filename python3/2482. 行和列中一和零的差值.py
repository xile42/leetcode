class Solution:

    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:

        m, n = len(grid), len(grid[0])
        ans = [[0 for _ in range(n)] for _ in range(m)]
        rs = [sum(r) for r in grid]
        cs = [sum(c) for c in list(zip(*grid))]

        for i in range(m):
            for j in range(n):
                ans[i][j] = 2 * rs[i] + 2 * cs[j] - m - n

        return ans
