class Solution:

    def longestSubarray(self, nums: List[int]) -> int:

        target = max(nums)

        result = 0
        idx = 0
        while idx < len(nums):

            if nums[idx] == target:
                count = 1
                while idx+1 < len(nums) and nums[idx+1] == target:
                    idx += 1
                    count += 1
                result = max(result, count)
                idx += 1

            else:
                idx += 1

        return result
