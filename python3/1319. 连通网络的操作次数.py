class Solution:

    def makeConnected(self, n: int, connections: List[List[int]]) -> int:

        vis = [False] * n
        g = [[] for _ in range(n)]
        for u, v in connections:
            g[v].append(u)
            g[u].append(v)

        if len(connections) < n - 1:
            return -1

        def f(i):

            vis[i] = True
            for j in g[i]:
                if not vis[j]:
                    f(j)

        ans = -1
        for i in range(n):
            if not vis[i]:
                f(i)
                ans += 1

        return ans
