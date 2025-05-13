class Solution:

    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:

        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        ans = 1
        s = set(restricted)
        vis = [False] * n

        def f(i):

            nonlocal ans
            vis[i] = True
            for j in g[i]:
                if not vis[j] and j not in s:
                    ans += 1
                    f(j)

        f(0)

        return ans
