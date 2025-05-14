class Solution:

    def maxSubarrays(self, nums: List[int]) -> int:

        s = reduce(and_, nums)
        if s:
            return 1
        cur = -1
        ans = 0
        for x in nums:
            cur &= x
            if cur == 0:
                ans += 1
                cur = -1

        return ans
