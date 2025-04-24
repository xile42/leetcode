class Solution:

    def massage(self, nums: List[int]) -> int:

        n = len(nums)

        @cache
        def f(i):

            if i >= n:
                return 0

            return max(nums[i] + f(i + 2), f(i + 1))

        return f(0)
