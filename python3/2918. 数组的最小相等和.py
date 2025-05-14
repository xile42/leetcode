class Solution:

    def minSum(self, nums1: List[int], nums2: List[int]) -> int:

        s1, s2 = sum(nums1), sum(nums2)
        z1, z2 = nums1.count(0), nums2.count(0)
        m1, m2 = s1 + z1, s2 + z2

        if z1 == 0 and z2 == 0:
            return -1 if s1 != s2 else s1
        elif z1 == 0:
            return -1 if m1 < m2 else m1
        elif z2 == 0:
            return -1 if m2 < m1 else m2

        return max(m1, m2)