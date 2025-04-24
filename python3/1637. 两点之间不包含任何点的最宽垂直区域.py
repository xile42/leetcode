class Solution:

    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:

        sx = sorted([xy[0] for xy in points])

        return max([sx[i] - sx[i - 1] for i in range(1, len(sx))])
