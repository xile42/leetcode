class Solution:

    def gcdOfOddEvenSums(self, n: int) -> int:

        a = b = 0

        i = 1
        for _ in range(n):
            a += i
            i += 2

        i = 2
        for _ in range(n):
            b += i
            i += 2

        return gcd(a, b)
