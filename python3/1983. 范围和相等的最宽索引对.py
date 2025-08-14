class Solution:

    def widestPairOfIndices(self, nums1: List[int], nums2: List[int]) -> int:

        pre_a = list(accumulate(nums1))
        pre_b = list(accumulate(nums2))
        pre = [i - j for i, j in zip(pre_a, pre_b)]
        d = dict()
        d[0] = -1
        ans = 0
        for i, v in enumerate(pre):
            if v in d:
                ans = max(ans, i - d[v])
            else:
                d[v] = i

        return ans
