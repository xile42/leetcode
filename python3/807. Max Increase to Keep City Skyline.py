class Solution:

    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        r_max = [max(grid[i]) for i in range(m)]
        c_max = [max([grid[i][j] for i in range(m)]) for j in range(n)]

        result = 0
        for idx in range(m):
            for jdx in range(n):
                max_value = min(r_max[idx], c_max[jdx])
                result += 0 if max_value <= grid[idx][jdx] else max_value - grid[idx][jdx]

        return result
