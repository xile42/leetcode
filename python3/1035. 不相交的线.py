class Solution:

    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:

        m = len(nums1)
        n = len(nums2)

        @cache
        def f(i, j):

            if i >= m or j >= n:
                return 0

            ans = -inf
            if nums1[i] == nums2[j]:
                ans = max(ans, 1 + f(i + 1, j + 1))
            ans = max(ans, f(i + 1, j), f(i, j + 1))

            return ans

        return f(0, 0)
