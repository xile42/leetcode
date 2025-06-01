class Solution:

    def maximumDetonation(self, bombs: List[List[int]]) -> int:

        def check(xyr1, xyr2):

            x1, y1, r1 = xyr1
            x2, y2, r2 = xyr2
            dis = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

            return (True if dis <= r1 else False, True if dis <= r2 else False)

        n = len(bombs)
        g = [[] for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                ij, ji = check(bombs[i], bombs[j])
                if ij:
                    g[i].append(j)
                if ji:
                    g[j].append(i)

        def f(i):

            vis[i] = True
            ans = 1
            for j in g[i]:
                if not vis[j]:
                    ans += f(j)

            return ans

        ans = 0
        for i in range(n):
            vis = [False] * n
            ans = max(ans, f(i))

        return ans
