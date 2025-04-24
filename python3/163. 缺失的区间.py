class Solution:

    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:

        ans = list()
        mn, mx = None, None
        for i, n in enumerate(nums):
            if n < lower or n > upper:
                continue
            if mx is not None and n - mx > 1:
                ans.append([mx + 1, n - 1])
            if mn is None:
                mn = n
            mx = n

        if mn is not None and mn > lower:
            ans = [[lower, mn - 1]] + ans
        if mx is not None and mx < upper:
            ans = ans + [[mx + 1, upper]]

        return [[lower, upper]] if mn is None and mx is None else ans
