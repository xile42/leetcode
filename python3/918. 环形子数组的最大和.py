class Solution:

    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        s = sum(nums)
        n = len(nums)
        mx = [0] * n
        mx[0] = nums[0]
        mn = [0] * n
        mn[0] = nums[0]

        for i in range(1, n):
            mx[i] = max(mx[i - 1], 0) + nums[i]
            mn[i] = min(mn[i - 1], 0) + nums[i]

        ans = max(max(mx), -inf if min(mn) == s else s - min(mn))

        return ans
