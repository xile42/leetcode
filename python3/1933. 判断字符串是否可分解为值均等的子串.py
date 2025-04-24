class Solution:

    def isDecomposable(self, s: str) -> bool:

        c = Counter([len(list(ite)) % 3 for _, ite in groupby(s)])

        return set(c.keys()) in [{2, 0}, {2}] and c[2] == 1
