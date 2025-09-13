class Solution:

    def swimInWater(self, grid: List[List[int]]) -> int:

        n = len(grid)
        vis = set()
        h = list()
        h.append((grid[0][0], 0, 0))
        cur = 0
        while h:
            t, x, y = heapq.heappop(h)
            vis.add((x, y))
            cur = max(cur, t)
            if x == n - 1 and y == n - 1:
                return cur
            for xx, yy in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
                if 0 <= xx < n and 0 <= yy < n and (xx, yy) not in vis:
                    heappush(h, (grid[xx][yy], xx, yy))
