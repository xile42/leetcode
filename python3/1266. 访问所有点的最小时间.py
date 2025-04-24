class Solution:

    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:

        ans = 0
        for (x, y), (xx, yy) in pairwise(points):
            xd = abs(x - xx)
            yd = abs(y - yy)
            ans += min(yd, xd) + abs(xd - yd)

        return ans
