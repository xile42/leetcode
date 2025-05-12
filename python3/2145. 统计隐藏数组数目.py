class Solution:

    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:

        mn, mx = 0, 0
        cur = 0
        for d in differences:
            cur += d
            mn = min(mn, cur)
            mx = max(mx, cur)

        diff1 = mx - mn
        diff2 = upper - lower

        return max(diff2 - diff1 + 1, 0)
