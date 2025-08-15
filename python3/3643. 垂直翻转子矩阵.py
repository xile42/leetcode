class Solution:

    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:

        cp = [row[:] for row in grid]

        for i in range(x, x + k):
            for j in range(y, y + k):
                grid[i][j] = cp[k - 1 - (i - x) + x][j]

        return grid
