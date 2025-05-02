class Solution:
    def findValidPair(self, s: str) -> str:
        c = Counter(s)
        for i, j in pairwise(s):
            if i != j and int(i) == c[i] and int(j) == c[j]:
                return i + j

        return str()