class Solution:

    def minCost(self, costs: List[List[int]]) -> int:

        n = len(costs)

        @cache
        def f(i, c):

            if i >= n:
                return 0

            ans = inf
            for cur in range(3):
                if cur == c:
                    continue
                ans = min(ans, costs[i][cur] + f(i + 1, cur))

            return ans

        ans = f(0, -1)

        return ans
