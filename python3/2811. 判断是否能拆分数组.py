class Solution:

    def canSplitArray(self, nums: List[int], m: int) -> bool:

        for a, b in pairwise(nums):
            if a + b >= m:
                return True

        return len(nums) <= 2
