class Solution:

    def countPairs(self, n: int, edges: List[List[int]]) -> int:

        vis = [False] * n
        g = [[] for _ in range(n)]

        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        def f(node):

            vis[node] = True
            size = 1
            for next_node in g[node]:
                if not vis[next_node]:
                    size += f(next_node)

            return size

        ans = cur = 0
        for i in range(n):
            if not vis[i]:
                size = f(i)
                ans += size * cur
                cur += size

        return ans
