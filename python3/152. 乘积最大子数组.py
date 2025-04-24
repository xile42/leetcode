class Solution:

    def maxProduct(self, nums: List[int]) -> int:

        dp1 = [0] * len(nums)
        dp2 = [0] * len(nums)
        dp1[0] = dp2[0] = nums[0]
        for i in range(1, len(nums)):
            candidates = [dp1[i - 1] * nums[i], dp2[i - 1] * nums[i], nums[i]]
            dp1[i] = max(candidates)
            dp2[i] = min(candidates)

        return max(max(dp1), max(dp2))
