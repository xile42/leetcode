class Solution:

    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:

        s = set(nums1) & set(nums2)
        if s:
            return sorted(s)[0]

        a, b = min(nums1), min(nums2)
        if a > b:
            a, b = b, a
        return int(str(a) + str(b))
