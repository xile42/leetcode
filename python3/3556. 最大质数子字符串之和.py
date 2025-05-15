class Solution:

    def sumOfLargestPrimes(self, s: str) -> int:

        ss = set()
        for i in range(len(s)):
            for j in range(i, len(s)):
                ss.add(int(s[i:j + 1]))

        def is_prime(num):

            if num < 2:
                return False

            for i in range(2, isqrt(num) + 1):
                if num % i == 0:
                    return False

            return True

        ns = sorted([num for num in ss if is_prime(num)])

        return 0 if not ns else sum(ns[-3:])
