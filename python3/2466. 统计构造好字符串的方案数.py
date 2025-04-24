class Solution:

    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:

        base = pow(10, 9) + 7

        @cache
        def f(n):

            if n < 0:
                return 0

            if n == 0:
                return 1

            return (f(n-zero) + f(n-one)) % base

        result = 0
        for i in range(low, high+1):
            result += f(i)
            result %= base

        return result
