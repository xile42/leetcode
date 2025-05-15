class Solution:

    def maxFreqSum(self, s: str) -> int:

        c = Counter(s)
        mx1 = mx2 = 0
        for c, v in c.items():
            if c in "aeiou":
                mx1 = max(mx1, v)
            else:
                mx2 = max(mx2, v)

        return mx1 + mx2
