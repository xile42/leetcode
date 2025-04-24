class Solution:

    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        ans = 0
        for c, ite in groupby(nums):
            if c == 1:
                ans = max(ans, len(list(ite)))

        return ans
