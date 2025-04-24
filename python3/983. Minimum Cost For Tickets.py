class Solution:

    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        n = len(days)
        dp = [float("inf")] * (n+1)
        dp[0] = 0
        for idx in range(n):
            for jdx in range(idx, n):
                if days[jdx] - days[idx] <= 6:
                    dp[jdx+1] = min(dp[idx] + costs[1], dp[jdx+1])
                else:
                    break
            for jdx in range(idx, n):
                if days[jdx] - days[idx] <= 29:
                    dp[jdx+1] = min(dp[idx] + costs[2], dp[jdx+1])
                else:
                    break
            dp[idx+1] = min(dp[idx+1], dp[idx] + costs[0])

        return dp[-1]
