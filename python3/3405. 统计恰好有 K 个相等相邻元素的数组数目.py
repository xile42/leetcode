class Solution:

    def countGoodArrays(self, n: int, m: int, k: int) -> int:

        MOD = 1_000_000_007

        return comb(n - 1, k) % MOD * m * pow(m - 1, n - k - 1, MOD) % MOD
