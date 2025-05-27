class Solution:

    def countGoodNumbers(self, n: int) -> int:

        MOD = 10 ** 9 + 7
        a = pow(5, (n + 1) // 2, MOD)
        b = pow(4, n // 2, MOD)

        return (a * b) % MOD
