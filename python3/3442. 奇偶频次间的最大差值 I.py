class Solution:
    def maxDifference(self, s: str) -> int:
        c = Counter(s)
        j, o = list(), list()
        for v in c.values():
            if v & 1:
                j.append(v)
            else:
                o.append(v)

        return max(j) - min(o)