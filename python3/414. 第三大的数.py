class Solution:

    def thirdMax(self, nums: List[int]) -> int:

        sn = sorted(set(nums))

        return sn[-1] if len(sn) < 3 else sn[-3]
