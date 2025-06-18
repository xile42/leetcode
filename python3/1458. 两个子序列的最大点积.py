class Solution:

    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:

        @cache
        def f(i, j):

            if i < 0 or j < 0:
                return -inf

            if i == 0 and j == 0:
                return nums1[0] * nums2[0]

            return max(f(i - 1, j), f(i, j - 1), f(i - 1, j - 1), f(i - 1, j - 1) + nums1[i] * nums2[j], nums1[i] * nums2[j])

        return f(len(nums1) - 1, len(nums2) - 1)
