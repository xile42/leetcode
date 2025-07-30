class Solution:

    def findMinArrowShots(self, points: List[List[int]]) -> int:

        points.sort(key=lambda p: p[1])
        ans = 0
        pre = -inf
        for start, end in points:
            if start > pre:
                ans += 1
                pre = end

        return ans
