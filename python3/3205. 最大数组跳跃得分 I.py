class Solution:

    def maxScore(self, nums: List[int]) -> int:

        n = len(nums)

        @cache
        def f(i):

            if i >= n - 1:
                return 0

            ans = 0
            for j in range(i + 1, n):
                ans = max(ans, (j - i) * nums[j] + f(j))

            return ans

        ans = f(0)
        f.cache_clear()

        return ans
