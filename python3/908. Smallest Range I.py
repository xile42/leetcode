class Solution:

    def smallestRangeI(self, nums: List[int], k: int) -> int:

        return max(max(nums) - min(nums) - k * 2, 0)
