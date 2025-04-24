class Solution:

    def isConsecutive(self, nums: List[int]) -> bool:

        n = len(nums)
        sn = sorted(nums)

        return n == len(set(nums)) and sn[-1] == sn[0] + n - 1
