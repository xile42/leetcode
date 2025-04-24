class Solution:

    def maxSales(self, sales: List[int]) -> int:

        n = len(sales)
        dp = [-inf] * n
        for i, v in enumerate(sales):
            if i == 0:
                dp[i] = v
            else:
                dp[i] = max(0, dp[i - 1]) + v

        return max(dp)
