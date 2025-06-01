class Solution:

    def minScore(self, n: int, roads: List[List[int]]) -> int:

        dis = [inf] * (n + 1)
        dis[1] = 0
        g = [[] for _ in range(n + 1)]
        for u, v, w in roads:
            g[u].append([v, w])
            g[v].append([u, w])

        def f(i, cur):

            dis[i] = cur
            for j, w in g[i]:
                d = min(cur, w)
                if d < dis[j]:
                    f(j, d)

        f(1, inf)

        return dis[-1]
