class Solution:

    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        g = defaultdict(list)
        for u, v in connections:
            g[u].append(v)
            g[v].append(-u)

        ans = 0
        vis = [False] * n

        def f(i):

            nonlocal ans
            vis[i] = True
            for j in g[i]:
                if vis[abs(j)]:
                    continue
                if j > 0:
                    ans += 1
                f(abs(j))

        f(0)

        return ans
