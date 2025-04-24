class Solution:

    def longestSubarray(self, nums: List[int]) -> int:

        left = ans = 0
        chance = 1
        for right, n in enumerate(nums):
            chance += -1 if n == 0 else 0
            while chance < 0:
                if nums[left] == 0:
                    chance += 1
                left += 1
            ans = max(ans, right - left)

        return ans
