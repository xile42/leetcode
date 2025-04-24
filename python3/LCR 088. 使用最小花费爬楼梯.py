class Solution:

    def minCostClimbingStairs(self, cost: List[int]) -> int:

        cost.append(0)
        
        @cache
        def f(n):

            if n < 0:
                return 0

            return cost[n] + min(f(n - 1), f(n - 2))

        return f(len(cost) - 1)
