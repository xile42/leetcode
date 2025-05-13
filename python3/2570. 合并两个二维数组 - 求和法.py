class Solution:

    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:

        c = Counter()
        for a, b in nums1:
            c[a] += b
        for a, b in nums2:
            c[a] += b

        return sorted(list(c.items()))
