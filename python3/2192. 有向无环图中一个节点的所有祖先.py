class Solution:

    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        g = [[] for _ in range(n)]
        for u, v in edges:
            g[v].append(u)
        vis = [False] * n
        ans = [set() for _ in range(n)]

        @cache
        def f(i):

            this_ans = set()
            for j in g[i]:
                this_ans |= f(j)

            if not vis[i]:
                ans[i] |= this_ans
                vis[i] = True
            this_ans.add(i)

            return this_ans

        for i in range(n):
            if not vis[i]:
                f(i)

        ans = [sorted(i) for i in ans]
        f.cache_clear()

        return ans
