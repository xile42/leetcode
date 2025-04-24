class Solution:

    def maxSubArray(self, nums: List[int]) -> int:

        n = len(nums)
        dp = [0] * n
        for i, v in enumerate(nums):
            dp[i] = v if i == 0 else max(0, dp[i - 1]) + v

        return max(dp)
