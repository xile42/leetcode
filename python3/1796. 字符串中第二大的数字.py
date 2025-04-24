class Solution:

    def secondHighest(self, s: str) -> int:

        d = set([int(c) for c in s if c.isdigit()])
        d = sorted(d)

        return -1 if len(d) < 2 else d[-2]
