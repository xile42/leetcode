class Solution:

    def findLength(self, nums1: List[int], nums2: List[int]) -> int:

        @cache
        def f(i, j):

            if i < 0 or j < 0:
                return 0

            return 0 if nums1[i] != nums2[j] else f(i - 1, j - 1) + 1

        ans = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                ans = max(ans, f(i, j))
        f.cache_clear()

        return ans
