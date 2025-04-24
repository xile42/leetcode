class Solution:

    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:

        min_d = inf
        ans = None
        for i, (xx, yy) in enumerate(points):
            if xx == x or yy == y:
                d = max(abs(y - yy), abs(x - xx))
                if d < min_d:
                    min_d = d
                    ans = i

        return ans if ans is not None else -1
