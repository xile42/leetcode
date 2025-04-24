class NeighborSum:

    def __init__(self, grid: List[List[int]]):

        self.g = grid
        self.m = len(grid)
        self.n = len(grid[0])

    def adjacentSum(self, value: int) -> int:

        for i in range(self.m):
            for j in range(self.n):
                if self.g[i][j] == value:
                    break
            if self.g[i][j] == value:
                    break

        result = 0
        for ii, jj in (i-1, j), (i+1, j), (i, j-1), (i, j+1):
            if not (0 <= ii < self.m and 0 <= jj < self.n):
                continue
            result += self.g[ii][jj]

        return result

    def diagonalSum(self, value: int) -> int:
        
        for i in range(self.m):
            for j in range(self.n):
                if self.g[i][j] == value:
                    break
            if self.g[i][j] == value:
                break    

        result = 0
        for ii, jj in (i-1, j-1), (i+1, j+1), (i-1, j+1), (i+1, j-1):
            if not (0 <= ii < self.m and 0 <= jj < self.n):
                continue
            result += self.g[ii][jj]

        return result

# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)
