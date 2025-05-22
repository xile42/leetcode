class Solution:

    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:

        ans = 1
        ns = [xy[0] for xy in points]
        ns.sort()
        cur = ns[0] + w
        for n in ns:
            if n > cur:
                ans += 1
                cur = n + w

        return ans
