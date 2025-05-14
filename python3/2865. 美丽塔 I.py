class Solution:

    def maximumSumOfHeights(self, heights: List[int]) -> int:

        def f(ns, limit):

            ans = 0
            for n in ns:
                ans += min(n, limit)
                limit = min(limit, n)

            return ans

        ans = -inf
        for i, v in enumerate(heights):
            ans = max(ans, v + f(heights[:i][::-1], v) + f(heights[i + 1:], v))

        return ans
