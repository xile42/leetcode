class Solution:

    def isMonotonic(self, nums: List[int]) -> bool:

        diff = [nums[i] - nums[i - 1] for i in range(1, len(nums))]

        return all(i >= 0 for i in diff) or all(i <= 0 for i in diff)
