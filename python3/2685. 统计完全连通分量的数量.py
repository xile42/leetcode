class Solution:

    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:

        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        vis = [False] * n

        def f(i):

            nonlocal s, e
            vis[i] = True
            s += 1
            e += len(g[i])
            for j in g[i]:
                if not vis[j]:
                    f(j)

        ans = 0
        for i in range(n):
            if not vis[i]:
                s = e = 0
                f(i)
                if e == 2 * (s * (s - 1) // 2):
                    ans += 1

        return ans
