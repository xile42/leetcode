class Solution:

    def maxSumDivThree(self, nums: List[int]) -> int:

        s = sum(nums)
        if s % 3 == 0:
            return s
        a1 = sorted(x for x in nums if x % 3 == 1)
        a2 = sorted(x for x in nums if x % 3 == 2)
        if s % 3 == 2:
            a1, a2 = a2, a1
        ans = s - a1[0] if a1 else 0
        if len(a2) > 1:
            ans = max(ans, s - a2[0] - a2[1])

        return ans
