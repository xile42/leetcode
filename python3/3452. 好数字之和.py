class Solution:

    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:

        ans = 0
        for i, n in enumerate(nums):
            if i - k >= 0 and nums[i - k] >= n:
                continue
            if i + k < len(nums) and nums[i + k] >= n:
                continue
            ans += n

        return ans