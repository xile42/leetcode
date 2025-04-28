class Solution:

    def baseUnitConversions(self, conversions: List[List[int]]) -> List[int]:

        n = len(conversions) + 1
        g = defaultdict(list)
        for u, v, w in conversions:
            g[u].append([v, w])

        base = 10 ** 9 + 7
        vis = [False] * n
        ans = [-1] * n
        q = [[0, 1]]
        while q:
            cur, v = q.pop(0)
            vis[cur] = True
            ans[cur] = v % base
            for other, w in g[cur]:
                if vis[other]:
                    continue
                q.append([other, v * w % base])

        return ans
