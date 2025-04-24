class Solution:

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        vis = [False] * n
        success = False

        def f(u):
            nonlocal success
            vis[u] = True
            if success:
                return
            for v in g[u]:
                if v == destination:
                    success = True
                    return
                if not vis[v]:
                    f(v)

        f(source)

        return success or source == destination
