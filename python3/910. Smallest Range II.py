class Solution:

    def smallestRangeII(self, nums: List[int], k: int) -> int:

        nums.sort()
        result = nums[-1] - nums[0]
        for i, j in pairwise(nums):
            max_value = max(i + k, nums[-1] - k)
            min_value = min(nums[0] + k, j - k)
            result = min(result, max_value - min_value)

        return result
