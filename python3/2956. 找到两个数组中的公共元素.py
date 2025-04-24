class Solution:

    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:

        c1 = Counter(nums1)
        c2 = Counter(nums2)
        ans1 = ans2 = 0
        for k in c1:
            ans1 += 0 if k not in c2 else c1[k]
        for k in c2:
            ans2 += 0 if k not in c1 else c2[k]

        return [ans1, ans2]
