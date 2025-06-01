class Solution:

    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:

        nums1.sort()
        idxs = sorted(range(len(nums2)), key=lambda x: nums2[x])

        ans = [-1] * len(nums1)
        i = 0
        j = len(nums2) - 1
        for n in nums1:
            if n > nums2[idxs[i]]:
                ans[idxs[i]] = n
                i += 1
            else:
                ans[idxs[j]] = n
                j -= 1

        return ans
