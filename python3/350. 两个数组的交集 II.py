class Solution:

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        ans = list()
        for k, v in (Counter(nums1) & Counter(nums2)).items():
            ans += [k] * v

        return ans
