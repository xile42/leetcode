class Solution:

    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:

        d = defaultdict(lambda: 0)
        for i, (xx, yy) in enumerate(zip(x, y)):
            d[xx] = max(d[xx], yy)

        if len(d) < 3:
            return -1

        return sum(sorted(d.values())[-3:])
