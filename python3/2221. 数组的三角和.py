class Solution:

    def triangularSum(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        ans = 0
        n = len(nums)
        for i, v in enumerate(nums):
            ans += comb(n - 1, i) * v % 10

        return ans % 10
