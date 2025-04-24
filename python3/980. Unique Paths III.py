class Solution:

    result = 0

    def search(self, i, j, mask):

        if self.grid[i][j] == 2 and mask.bit_count() == self.target_count-1:
            self.result += 1
            return

        for ii, jj in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
            if 0 <= ii < self.m and 0 <= jj < self.n and self.grid[ii][jj] != -1 and (mask & (1 << (ii*self.n+jj)) == 0):
                self.search(ii, jj, mask | (1 << (i*self.n+j)))

    def uniquePathsIII(self, grid: List[List[int]]) -> int:

        self.m, self.n = len(grid), len(grid[0])
        self.grid = grid

        self.target_count = 0
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 1:
                    start_i, start_j = i, j
                if grid[i][j] != -1:
                    self.target_count += 1

        self.result = 0
        self.search(start_i, start_j, 0)

        return self.result
