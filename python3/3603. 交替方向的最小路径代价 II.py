fmin = lambda x, y: x if x < y else y
fmax = lambda x, y: x if x > y else y


class Solution:

    def minCost(self, m: int, n: int, waitCost: List[List[int]]) -> int:

        dp = [[inf for _ in range(n)] for _ in range(m)]
        dp[0][0] = 0

        entry_cost = lambda x, y: (x + 1) * (y + 1)

        for j in range(1, n):
            wait_cost = 0 if j == 1 else waitCost[0][j - 1]
            dp[0][j] = fmin(dp[0][j], dp[0][j - 1] + entry_cost(0, j) + wait_cost)

        for i in range(1, m):
            wait_cost = 0 if i == 1 else waitCost[i - 1][0]
            dp[i][0] = fmin(dp[i][0], dp[i - 1][0] + entry_cost(i, 0) + wait_cost)

        for i in range(1, m):
            for j in range(1, n):
                up = dp[i - 1][j] + entry_cost(i, j) + waitCost[i - 1][j]
                left = dp[i][j - 1] + entry_cost(i, j) + waitCost[i][j - 1]
                dp[i][j] = fmin(up, left)

        return dp[-1][-1] + 1
