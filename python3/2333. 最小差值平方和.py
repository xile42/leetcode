class Solution:

    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:

        k = k1 + k2
        c = [0] * (10 ** 5 + 1)
        for i in range(len(nums1)):
            c[abs(nums1[i] - nums2[i])] += 1

        for i in range(len(c) - 1, 0, -1):
            if not c[i]:
                continue
            diff = min(k, c[i])
            c[i] -= diff
            c[i - 1] += diff
            k -= diff
            if k == 0:
                break

        ans = sum([c[i] * (i ** 2) for i in range(1, len(c))])

        return ans
