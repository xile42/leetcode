class Solution:

    def findMaxK(self, nums: List[int]) -> int:

        for n in sorted(nums, reverse=True):
            
            if n <= 0:
                return -1

            if -n in nums:
                return n

        return -1
