class Solution:

    def longestEqualSubarray(self, nums: List[int], k: int) -> int:

        d = defaultdict(list)
        for i, n in enumerate(nums):
            d[n].append(i)

        ans = 0
        for ns in d.values():
            left = 0
            cur = 0
            for right, n in enumerate(ns):
                cur += 0 if right == 0 else n - ns[right - 1] - 1
                while cur > k:
                    cur -= ns[left + 1] - ns[left] - 1
                    left += 1
                ans = max(ans, right - left + 1)

        return ans
