class Solution:

    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:

        diff1 = [nums1[i] - nums2[i] for i in range(len(nums1))]
        base1 = sum(nums2)
        diff2 = [-i for i in diff1]
        base2 = sum(nums1)

        def f(ns):
            dp = [0] * len(ns)
            dp[0] = ns[0]
            for i in range(1, len(ns)):
                dp[i] = max(dp[i - 1], 0) + ns[i]
            return max(dp)

        return max(f(diff1) + base1, f(diff2) + base2)
