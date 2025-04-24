class Solution:

    def findClosestNumber(self, nums: List[int]) -> int:

        sn = sorted([[abs(i), -i] for i in nums])
        return -sn[0][-1]
