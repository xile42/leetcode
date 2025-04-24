class Solution:

    def rob(self, nums: List[int]) -> int:

        def f(nums):
            
            if len(nums) == 0:
                return 0
            
            dp = [0] * (len(nums) + 1)
            dp[1] = nums[0]
            if len(nums) == 1:
                return dp[1]
            
            for i in range(2, len(nums)+1):
                dp[i] = max(nums[i-1] + dp[i-2], dp[i-1])

            return dp[-1]

        result = max(nums[0] + f(nums[2:-1]), f(nums[1:]))

        return result
