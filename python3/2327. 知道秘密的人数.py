class Solution:

    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:

        MOD = 1_000_000_007
        diff = [0] * (n + 2)
        diff[1] = 1
        diff[2] = -1
        ans = known = 0

        for i in range(1, n + 1):
            known = (known + diff[i]) % MOD
            if i >= n - forget + 1:
                ans += known
            diff[min(i + delay, n + 1)] += known
            diff[min(i + forget, n + 1)] -= known

        return ans % MOD
