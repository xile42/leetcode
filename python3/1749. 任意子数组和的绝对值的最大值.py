class Solution:

    def maxAbsoluteSum(self, nums: List[int]) -> int:

        dp = nums.copy()
        for i in range(1, len(dp)):
            dp[i] = max(dp[i - 1], 0) + nums[i]
        ans1 = max(dp)

        dp = nums.copy()
        dp = [-i for i in dp]
        for i in range(1, len(dp)):
            dp[i] = max(dp[i - 1], 0) - nums[i]
        ans2 = max(dp)

        return max(ans1, ans2)
