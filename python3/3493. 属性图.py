class Solution:

    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:

        n = len(properties)
        s = [set(row) for row in properties]
        g = defaultdict(list)
        for i in range(n):
            for j in range(i + 1, n):
                cnt = len(s[i] & s[j])
                if cnt >= k:
                    g[i].append(j)
                    g[j].append(i)
        vis = [False for _ in range(n)]

        def f(i):

            vis[i] = True
            for j in g[i]:
                if not vis[j]:
                    f(j)

        ans = 0
        for i in range(n):
            if not vis[i]:
                ans += 1
                f(i)

        return ans
