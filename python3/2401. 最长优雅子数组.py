class Solution:

    def longestNiceSubarray(self, nums: List[int]) -> int:

        c = Counter()
        ans = left = 0
        for right in range(len(nums)):
            n = nums[right]
            for i in range(32):
                if n & (1 << i):
                    c[i] += 1
            while any(v > 1 for v in c.values()):
                n = nums[left]
                for i in range(32):
                    if n & (1 << i):
                        c[i] -= 1
                left += 1
            ans = max(ans, right - left + 1)

        return ans
