class Solution:

    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:

        n = len(nums1)
        base = 10 ** 9 + 7
        ns = sorted(nums1)
        vs = [abs(nums1[i] - nums2[i]) % base for i in range(n)]
        ans = s = sum(vs) % base
        for i in range(n):
            cur_value = vs[i]
            j = bisect_left(ns, nums2[i])
            new_n = ns[-1] if j == len(ns) else ns[j]
            new_value = abs(new_n - nums2[i])
            new_n = ns[0] if j == 0 else ns[j - 1]
            new_value = min(new_value, abs(new_n - nums2[i]))
            new_value %= base
            ans = min(ans, s - cur_value + new_value)

        return ans % base
