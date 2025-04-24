class Solution:

    def longestMonotonicSubarray(self, nums: List[int]) -> int:

        inc, dec = list(), list()

        for a, b in pairwise(nums):
            inc.append(1 if a < b else 0)
            dec.append(1 if a > b else 0)

        ans = 1
        for v, ite in groupby(inc):
            if v:
                ans = max(ans, len(list(ite)) + 1)
        for v, ite in groupby(dec):
            if v:
                ans = max(ans, len(list(ite)) + 1)

        return ans
