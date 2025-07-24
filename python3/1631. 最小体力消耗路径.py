class Solution:

    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        m, n = len(heights), len(heights[0])
        dis = [[inf for _ in range(n)] for _ in range(m)]
        dis[0][0] = 0
        heap = [(0, 0, 0)]

        while heap:
            x, y, d = heappop(heap)
            if d > dis[x][y]:
                continue
            for xx, yy in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
                if 0 <= xx < m and 0 <= yy < n:
                    new_d = max(d, abs(heights[x][y] - heights[xx][yy]))
                    if new_d < dis[xx][yy]:
                        dis[xx][yy] = new_d
                        heappush(heap, (xx, yy, new_d))

        return dis[-1][-1]
