class Solution:

    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:

        dp = [[0 for _ in range(n)] for _ in range(k + 1)]
        dp[k][0] = 1

        for day in range(k - 1, -1, -1):
            for s, t in relation:
                dp[day][t] += dp[day + 1][s]

        return dp[0][n - 1]
