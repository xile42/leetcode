class Solution:

    def minTimeToReach(self, moveTime: List[List[int]]) -> int:

        q = list()
        m, n = len(moveTime), len(moveTime[0])
        visit = [[float("inf") for _ in range(n)] for _ in range(m)]
        x, y = 0, 0
        t = 0
        visit[x][y] = 0
        q.append((x, y, t))
        while q:
            x, y, t = q.pop(0)
            for i, j in (x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1):
                if (not 0 <= i < m) or (not 0 <= j < n):
                    continue
                tt = max(moveTime[i][j] + 1, t + 1)
                if tt < visit[i][j]:
                    q.append((i, j, tt))
                    visit[i][j] = tt
                else:
                    continue

        return visit[m - 1][n - 1]