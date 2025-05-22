class Solution:

    def countAlternatingSubarrays(self, nums: List[int]) -> int:

        ans = left = 0
        n = len(nums)
        for right in range(n):
            if right > 0 and nums[right] == nums[right - 1]:
                left = right
            ans += right - left + 1

        return ans
