class Solution:

    def checkDivisibility(self, n: int) -> bool:

        a = 0
        b = 1
        for c in str(n):
            v = int(c)
            a += v
            b *= v

        return n % (a + b) == 0
