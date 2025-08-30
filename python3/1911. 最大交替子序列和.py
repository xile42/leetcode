class Solution:

    def maxAlternatingSum(self, nums: List[int]) -> int:

        n = len(nums)

        @cache
        def f(i, flag):

            if i >= n:
                return 0

            ans = 0
            ans = max(ans, f(i + 1, flag))
            ans = max(ans, nums[i] * flag + f(i + 1, -flag))

            return ans

        return f(0, 1)
