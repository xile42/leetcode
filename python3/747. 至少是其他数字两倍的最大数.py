class Solution:

    def dominantIndex(self, nums: List[int]) -> int:

        sn = sorted(nums)
        if sn[-1] >= sn[-2] * 2:
            return nums.index(sn[-1])

        return -1
