class Solution:

    def maxArrayValue(self, nums: List[int]) -> int:

        ans = max(nums)
        i = len(nums) - 1
        cur = nums[i]
        while i >= 1:
            if nums[i - 1] <= cur:
                cur += nums[i - 1]
                ans = max(ans, cur)
                i -= 1
            else:
                cur = nums[i - 1]
                i -= 1

        return ans
