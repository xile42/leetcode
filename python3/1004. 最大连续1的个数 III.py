class Solution:

    def longestOnes(self, nums: List[int], k: int) -> int:

        ans = left = 0
        chance = k
        for right, n in enumerate(nums):
            chance += -1 if n == 0 else 0
            while chance < 0:
                if nums[left] == 0:
                    chance += 1
                left += 1
            ans = max(ans, right - left + 1)

        return ans
