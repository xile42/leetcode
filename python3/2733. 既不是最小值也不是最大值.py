class Solution:

    def findNonMinOrMax(self, nums: List[int]) -> int:

        s = set(nums)

        return -1 if len(s) <= 2 else sorted(s)[1]
