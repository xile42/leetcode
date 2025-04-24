class Solution:

    def findMagicIndex(self, nums: List[int]) -> int:

        for i, v in enumerate(nums):
            if i == v:
                return i

        return -1
