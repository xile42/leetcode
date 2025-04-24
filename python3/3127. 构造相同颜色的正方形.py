class Solution:

    def canMakeSquare(self, grid: List[List[str]]) -> bool:

        def f(i, j):
            cnt = 0
            for ii, jj in (i, j), (i + 1, j), (i, j + 1), (i + 1, j + 1):
                if grid[ii][jj] == "B":
                    cnt += 1
            return True if cnt != 2 else False

        return f(0, 0) or f(0, 1) or f(1, 0) or f(1, 1)
