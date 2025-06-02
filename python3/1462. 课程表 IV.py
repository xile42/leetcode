class Solution:

    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        g = [[] for _ in range(n)]
        for u, v in prerequisites:
            g[u].append(v)
        is_pre = [[False for _ in range(n)] for _ in range(n)]
        vis = [False] * n

        def f(i):

            vis[i] = True
            for j in g[i]:
                is_pre[j][i] = True
                if not vis[j]:
                    f(j)
                for k in range(n):
                    is_pre[k][i] = is_pre[k][i] or is_pre[k][j]

        for i in range(n):
            f(i)

        ans = list()
        for i, j in queries:
            ans.append(is_pre[j][i])

        return ans
