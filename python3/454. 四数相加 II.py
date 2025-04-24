class Solution:

    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:

        cnt = Counter()
        for a, va in Counter(nums1).items():
            for b, vb in Counter(nums2).items():
                cnt[a + b] += va * vb

        ans = 0
        for c, vc in Counter(nums3).items():
            for d, vd in Counter(nums4).items():
                target = -(c + d)
                ans += cnt[target] * vc * vd

        return ans
