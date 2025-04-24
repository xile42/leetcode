class Solution:

    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:

        m, n = len(grid), len(grid[0])
        result = [[0 for _ in range(n)] for _ in range(m)]
        for idx in range(m):
            for jdx in range(n):
                index = (idx * n + jdx + k) % (m * n)
                x, y = index // n, index % n
                result[x][y] = grid[idx][jdx]

        return result
