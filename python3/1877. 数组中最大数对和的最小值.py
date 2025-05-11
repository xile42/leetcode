class Solution:

    def minPairSum(self, nums: List[int]) -> int:

        nums.sort()
        ans = -inf
        for i, n in enumerate(nums[:len(nums) // 2]):
            v = nums[len(nums) - 1 - i]
            ans = max(ans, n + v)

        return ans
