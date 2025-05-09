class Solution:

    def numPrimeArrangements(self, n: int) -> int:

        def is_prime(x):

            for i in range(2, isqrt(x) + 1):
                if x % i == 0:
                    return False

            return x > 1

        cnt = 0
        base = 10 ** 9 + 7
        for i in range(2, n + 1):
            if is_prime(i):
                cnt += 1

        return ((factorial(cnt) % base) * (factorial(n - cnt) % base)) % base
