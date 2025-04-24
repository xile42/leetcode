class Solution:

    def maxProductDifference(self, nums: List[int]) -> int:

        sn = sorted(nums)

        return sn[-1] * sn[-2] - sn[0] * sn[1]
