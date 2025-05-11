class Solution:

    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:

        c = Counter([min(w, l) for w, l in rectangles])

        return c[max(c.keys())]
