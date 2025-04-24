class Solution:

    def maxSum(self, nums: List[int]) -> int:

        d = dict()
        ans = -1
        for v in nums:
            n = max(str(v))
            if n in d:
                ans = max(ans, v + d[n])
            if n not in d or v > d[n]:
                d[n] = v

        return ans
