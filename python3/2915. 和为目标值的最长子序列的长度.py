class Solution:

    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:

        @cache
        def f(t, cur):

            if cur >= len(nums):
                return 0 if t == 0 else -inf

            if t < nums[cur]:
                return f(t, cur + 1)

            return max(f(t, cur + 1), f(t - nums[cur], cur + 1) + 1)

        result = f(target, 0)
        f.cache_clear()
        return max(result, -1)
