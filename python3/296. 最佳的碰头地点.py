class Solution:

    def minTotalDistance(self, grid: List[List[int]]) -> int:

        xs, ys = list(), list()
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if not grid[i][j]:
                    continue
                xs.append(i)
                ys.append(j)
        
        ans = 0
        sxs = sorted(xs)
        x = sxs[len(sxs) // 2] if len(sxs) & 1 else sum(sxs[len(sxs) // 2 - 1:len(sxs) // 2 + 1]) // 2
        sys = sorted(ys)
        y = sys[len(sys) // 2] if len(sys) & 1 else sum(sys[len(sys) // 2 - 1:len(sys) // 2 + 1]) // 2

        for i, j in zip(xs, ys):
            ans += abs(x - i) + abs(y - j)

        return ans
