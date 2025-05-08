class Solution:

    def countPrimeSetBits(self, left: int, right: int) -> int:

        def is_prime(x):
            for i in range(2, isqrt(x) + 1):
                if x % i == 0:
                    return False
            return x > 1

        ans = 0
        for i in range(left, right + 1):
            v = i.bit_count()
            if is_prime(v):
                ans += 1

        return ans
