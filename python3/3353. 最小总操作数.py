class Solution:

    def minOperations(self, nums: List[int]) -> int:

        ans = 0
        for a, b in pairwise(nums):
            if a != b:
                ans += 1

        return ans
