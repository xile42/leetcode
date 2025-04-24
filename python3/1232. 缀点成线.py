class Solution:

    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:

        coordinates.sort()

        return len(set([i[0] for i in coordinates])) == 1 or len(set([i[1] for i in coordinates])) == 1 or len(set([inf if y2 == y1 else (x2 - x1) / (y2 - y1) for (x1, y1), (x2, y2) in pairwise(coordinates)])) == 1
