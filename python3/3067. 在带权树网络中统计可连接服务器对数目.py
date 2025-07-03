class Solution:

    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:

        n = len(edges) + 1
        g = [[] for _ in range(n)]

        for u, v, w in edges:
            g[u].append((v, w))
            g[v].append((u, w))

        def f(u, parent, cur):

            ans = 0
            if cur % signalSpeed == 0:
                ans += 1

            for v, w in g[u]:
                if v != parent:
                    ans += f(v, u, cur + w)

            return ans

        ans = [0] * n
        for u in range(n):
            cur = 0
            for v, w in g[u]:
                v = f(v, u, w)
                ans[u] += cur * v
                cur += v

        return ans
