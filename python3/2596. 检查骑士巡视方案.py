class Solution:

    def checkValidGrid(self, grid: List[List[int]]) -> bool:

        d = dict()
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                d[grid[i][j]] = [i, j]

        x, y = d[0]
        if not (x == 0 and y == 0):
            return False
        for i in range(1, m * n):
            xx, yy = d[i]
            if {abs(x - xx), abs(y - yy)} != {1, 2}:
                return False
            x, y = xx, yy

        return True
