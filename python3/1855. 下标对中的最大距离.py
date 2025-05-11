class Solution:

    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:

        ans = 0
        for idx, v in enumerate(nums1):
            jdx = bisect_right(nums2, -v, key=lambda x: -x) - 1
            if jdx < 0:
                continue
            ans = max(ans, max(jdx - idx, 0))

        return ans
