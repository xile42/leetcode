class Solution:

    def findChampion(self, grid: List[List[int]]) -> int:

        n = len(grid)
        s = set(range(n))
        for i in range(n):
            for j in range(i + 1, n):
                if grid[i][j] and j in s:
                    s.remove(j)
                elif not grid[i][j] and i in s:
                    s.remove(i)

        return list(s)[0]
