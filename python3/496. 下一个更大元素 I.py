class Solution:

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        d = dict()
        for num in nums2:
            for k in d:
                if d[k] == -1 and k < num:
                    d[k] = num
            d[num] = -1

        return [d[i] for i in nums1]
