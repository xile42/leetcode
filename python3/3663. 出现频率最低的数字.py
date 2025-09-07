class Solution:

    def getLeastFrequentDigit(self, n: int) -> int:

        s = str(n)
        c = Counter(s)
        ns = sorted(c.items(), key=lambda x: (x[1], x[0]))

        return int(ns[0][0])
