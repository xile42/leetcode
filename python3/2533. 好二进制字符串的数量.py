class Solution:

    def goodBinaryStrings(self, minLength: int, maxLength: int, oneGroup: int, zeroGroup: int) -> int:
        
        base = pow(10, 9) + 7

        @cache
        def f(n):

            if n < 0:
                return 0

            if n == 0:
                return 1

            return (f(n-zeroGroup) + f(n-oneGroup)) % base

        result = 0
        for i in range(minLength, maxLength+1):
            result += f(i)
            result %= base

        return result
