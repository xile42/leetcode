class Solution:

    def findPermutationDifference(self, s: str, t: str) -> int:

        i1 = {c: i for i, c in enumerate(s)}
        i2 = {c: i for i, c in enumerate(t)}

        return  sum(abs(i1[k] - i2[k]) for k in s)
