class Solution:

    def minMalwareSpread(self, graph: List[List[int]], initial: List[int]) -> int:

        initial.sort()
        n = len(graph)
        vis = [False] * n
        d = dict()
        size = dict()

        def f(i, idx):

            vis[i] = True
            d[i] = idx
            ans = 1
            for j in range(n):
                if graph[i][j] and not vis[j]:
                    ans += f(j, idx)

            return ans

        idx = 0
        for i in initial:
            if not vis[i]:
                size[idx] = f(i, idx)
                idx += 1

        c = Counter([d[i] for i in initial])
        mn = 0
        ans = initial[0]
        for i in initial:
            idx = d[i]
            v = size[idx] if c[idx] == 1 else 0
            if v > mn:
                mn = v
                ans = i

        return ans
