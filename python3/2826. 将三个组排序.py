class Solution:

    def minimumOperations(self, nums: List[int]) -> int:

        @cache
        def f(cur, limit):

            if cur >= len(nums):
                return 0

            ans = inf
            ans = min(ans, f(cur + 1, limit) + 1)
            if nums[cur] >= limit:
                ans = min(ans, f(cur + 1, nums[cur]))

            return ans

        return f(0, -inf)
