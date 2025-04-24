class Solution:

    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:

        ans = 0
        left = 0
        while left < len(nums) and nums[left] > threshold:
            left += 1

        for right in range(left, len(nums)):
            if nums[right] <= threshold and (left == right or nums[right] & 1 != nums[right - 1] & 1):
                ans = max(ans, right - left + 1  - (nums[left] & 1))
                continue
            else:
                left = right if nums[right] <= threshold else right + 1
                continue

        return ans
