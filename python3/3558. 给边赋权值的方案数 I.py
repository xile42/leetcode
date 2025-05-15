base = 10 ** 9 + 7


class Solution:

    def assignEdgeWeights(self, edges: List[List[int]]) -> int:

        n = len(edges) + 1
        g = [[] for _ in range(n + 1)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        vis = [False] * (n + 1)
        mx_depth = 1

        def f(node, cur):

            nonlocal mx_depth
            mx_depth = max(mx_depth, cur)
            vis[node] = True
            for child in g[node]:
                if vis[child]:
                    continue
                f(child, cur + 1)

        f(1, 0)
        n = mx_depth

        return pow(2, n - 1) % base
