fmin = lambda x, y: x if x < y else y
fmax = lambda x, y: x if x > y else y


class Solution:

    def minTime(self, n: int, edges: List[List[int]]) -> int:

        g = [[] for _ in range(n)]
        for u, v, start, end in edges:
            g[u].append((v, start, end))

        dis = [inf] * n
        dis[0] = 0
        h = [(0, 0)]
        while h:
            t, x = heappop(h)
            if t > dis[x]:
                continue
            for y, start, end in g[x]:
                if t > end:
                    continue
                d = fmax(t, start) + 1
                if d < dis[y]:
                    dis[y] = d
                    heappush(h, (d, y))

        return dis[n - 1] if dis[n - 1] < inf else -1
