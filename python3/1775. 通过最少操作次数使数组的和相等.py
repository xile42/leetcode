class Solution:

    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:

        n1, n2 = len(nums1), len(nums2)
        s1, s2 = sum(nums1), sum(nums2)
        if n1 * 6 < n2 or n2 * 6 < n1:
            return -1

        ans = 0
        candidates = list()
        if s1 == s2:
            return 0
        elif s1 < s2:
            for v in nums1:
                candidates.append(6 - v)
            for v in nums2:
                candidates.append(v - 1)
        else:
            for v in nums2:
                candidates.append(6 - v)
            for v in nums1:
                candidates.append(v - 1)

        cur = 0
        candidates.sort(reverse=True)
        for v in candidates:
            cur += v
            ans += 1
            if cur >= abs(s1 - s2):
                return ans
