import heapq


class Solution:

    def minTimeToReach(self, moveTime: List[List[int]]) -> int:

        q = list()
        m, n = len(moveTime), len(moveTime[0])
        visit = [[float("inf") for _ in range(n)] for _ in range(m)]
        x, y = 0, 0
        t = 0
        f = 1
        visit[x][y] = 0
        heapq.heappush(q, (t, (x, y, t, f)))
        while q:
            _, (x, y, t, f) = heapq.heappop(q)
            ff = 2 if f == 1 else 1
            if t >= visit[m - 1][n - 1]:
                continue
            for i, j in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
                if (not 0 <= i < m) or (not 0 <= j < n):
                    continue
                tt = max(moveTime[i][j] + f, t + f)
                if tt < visit[i][j]:
                    heapq.heappush(q, (tt, (i, j, tt, ff)))
                    visit[i][j] = tt
                else:
                    continue

        return visit[m - 1][n - 1]
