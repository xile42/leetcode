class Solution:

    def countPoints(self, rings: str) -> int:

        d = defaultdict(set)
        for i in range(0, len(rings), 2):
            d[rings[i+1]].add(rings[i])

        return sum(len(v) == 3 for v in d.values())
