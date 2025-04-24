class Solution:

    def halvesAreAlike(self, s: str) -> bool:

        cs = "aeiouAEIOU"
        n = len(s) // 2
        c1 = Counter(s[:n])
        c2 = Counter(s[n:])

        r1 = r2 = 0
        for c in cs:
            r1 += c1[c]
            r2 += c2[c]

        return r1 == r2
