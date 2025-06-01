class Solution:

    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:

        c = [0] * n
        for u, v in roads:
            c[u] += 1
            c[v] += 1

        ns = sorted([[v, i] for i, v in enumerate(c)], key=lambda x: x[0])
        d = {i:v for i, v in zip([i[1] for i in ns], range(1, n + 1))}

        ans = 0
        for u, v in roads:
            ans += d[u] + d[v]

        return ans
