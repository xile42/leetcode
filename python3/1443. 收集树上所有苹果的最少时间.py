class Solution:

    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:

        ind = Counter()
        g = [[] for _ in range(n)]
        for u, v in edges:
            ind[v] += 1
            g[u].append(v)
            g[v].append(u)
        root = None
        for i in range(n):
            if ind[i] == 0:
                root = i
                break
        vis = [False] * n

        def dfs(cur):

            vis[cur] = True

            ans = 0
            for child in g[cur]:
                if vis[child]:
                    continue
                res = dfs(child)
                if res != -inf:
                    ans += res

            return ans + 2 if ans > 0 or hasApple[cur] else -inf

        ans = dfs(root)

        return 0 if ans == -inf else ans - 2
