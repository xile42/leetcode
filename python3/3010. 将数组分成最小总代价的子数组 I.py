class Solution:

    def minimumCost(self, nums: List[int]) -> int:

        return sum(sorted(nums[1:])[:2]) + nums[0]
