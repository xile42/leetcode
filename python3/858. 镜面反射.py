class Solution:

    def mirrorReflection(self, p: int, q: int) -> int:

        x = gcd(p, q)
        p //= x
        q //= x

        if p & 1 and q & 1:
            return 1
        if p & 1 and not q & 1:
            return 0
        if not p & 1 and q & 1:
            return 2
