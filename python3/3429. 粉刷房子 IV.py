class Solution:

    def minCost(self, n: int, cost: List[List[int]]) -> int:

        status = [[-1 for _ in range(n // 2)] for _ in range(2)]
        colors = [0, 1, 2]

        @cache
        def f(i, j, k):

            if i == n // 2:
                return 0

            valid_cs = list()
            for c1 in colors:
                for c2 in colors:
                    if c1 != c2 and c1 != j and c2 != k:
                        valid_cs.append([c1, c2])

            ans = inf
            for c1, c2 in valid_cs:
                ans = min(ans, cost[i][c1] + cost[n - 1 - i][c2] + f(i + 1, c1, c2))

            return ans

        res = f(0, -1, -1)

        return res
