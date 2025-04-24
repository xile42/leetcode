class Solution:

    def hasTrailingZeros(self, nums: List[int]) -> bool:

        return len([i for i in nums if i & 1 == 0]) >= 2
