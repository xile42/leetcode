class Solution:

    def maxStrength(self, nums: List[int]) -> int:

        n = len(nums)
        dp = [[-inf, inf] for _ in range(n)]
        dp[0][0] = nums[0]
        dp[0][1] = nums[0]

        for i, v in enumerate(nums):
            if i == 0:
                continue
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][0] * v, dp[i - 1][1] * v, v)
            dp[i][1] = min(dp[i - 1][1], dp[i - 1][1] * v, dp[i - 1][0] * v, v)

        return dp[-1][0]
