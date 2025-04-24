class Solution:

    def semiOrderedPermutation(self, nums: List[int]) -> int:

        n = len(nums)
        i, j = nums.index(1), nums.index(n)
        ans = i + n - j - 1
        if i > j:
            ans -= 1

        return ans
