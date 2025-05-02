class Solution:

    def countSubarrays(self, nums: List[int]) -> int:
        ans = 0
        for i in range(2, len(nums)):
            a, b, c = nums[i - 2], nums[i - 1], nums[i]
            if 2 * (a + c) == b:
                ans += 1

        return ans