class Solution:

    def treeDiameter(self, edges: List[List[int]]) -> int:
        """
        :type root: 'Node'
        :rtype: int
        """

        graph = [set() for _ in range(len(edges) + 1)]
        for edge in edges:
            u, v = edge
            graph[u].add(v)
            graph[v].add(u)

        ans = 0
        vis = defaultdict(lambda: False)

        def f(node):

            nonlocal ans
            vis[node] = True

            ls = [f(other) for other in graph[node] if not vis[other]]
            ls.sort()
            if ls:
                ans = max(ans, ls[-1])
            if len(ls) >= 2:
                ans = max(ans, sum(ls[-2:]))

            return 1 if not ls else max(ls) + 1

        f(0)

        return ans
