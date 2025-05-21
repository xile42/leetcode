class Solution:

    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:

        c1 = Counter(nums1)
        c2 = Counter(nums2)

        nums2.sort()
        start2 = nums2[0]
        ans = inf
        for start1 in sorted(c1.keys())[:3]:
            x = start2 - start1
            for n in nums2:
                if c1[n - x] >= c2[n]:
                    continue
                else:
                    break
            else:
                ans = min(ans, x)

        return ans
