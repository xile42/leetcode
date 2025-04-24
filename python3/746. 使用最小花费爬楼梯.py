class Solution:

    def minCostClimbingStairs(self, cost: List[int]) -> int:

        dp = [0, 0]
        for idx in range(2, len(cost) + 1):
            dp.append(min(dp[idx-1]+cost[idx-1], dp[idx-2]+cost[idx-2]))

        return dp[-1]
