class Solution:

    def longestSubsequence(self, nums: List[int]) -> int:

        if set(nums) == {0}:
            return 0

        c = Counter()
        for n in nums:
            i = 0
            while n:
                if n & 1:
                    c[i] += 1
                n >>= 1
                i += 1

        ans = len(nums)
        for v in c.values():
            if v & 1:
                return ans

        return ans - 1
