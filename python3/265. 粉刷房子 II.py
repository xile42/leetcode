class Solution:

    def minCostII(self, costs: List[List[int]]) -> int:

        n = len(costs)
        k = len(costs[0])

        @cache
        def f(i, pre):

            if i >= n:
                return 0

            ans = inf
            for j in range(k):
                if j != pre:
                    ans = min(ans, costs[i][j] + f(i + 1, j))

            return ans

        ans = f(0, -1)
        f.cache_clear()

        return ans
