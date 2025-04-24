class Solution:

    def areAlmostEqual(self, s1: str, s2: str) -> bool:

        n = len(s1)
        diffi = [i for i in range(n) if s1[i] != s2[i]]
        c1 = [s1[i] for i in diffi]
        c2 = [s2[i] for i in diffi]

        if sorted(c1) == sorted(c2) and len(c1) in [0, 2]:
            return True

        return False
