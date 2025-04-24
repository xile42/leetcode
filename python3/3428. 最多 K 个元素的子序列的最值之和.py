MOD = 1_000_000_007
MX = 100_000

fac = [0] * MX  # f[i] = i!
fac[0] = 1
for i in range(1, MX):
    fac[i] = fac[i - 1] * i % MOD

inv_f = [0] * MX  # inv_f[i] = i!^-1
inv_f[-1] = pow(fac[-1], -1, MOD)
for i in range(MX - 1, 0, -1):
    inv_f[i - 1] = inv_f[i] * i % MOD

def comb(n: int, m: int) -> int:
    return fac[n] * inv_f[m] * inv_f[n - m] % MOD


class Solution:

    def minMaxSums(self, nums: List[int], k: int) -> int:

        max_k = k
        sn = sorted(nums)
        ans = 0

        for i, cur in enumerate(sn):
            cur_max = sn[len(sn) - 1 - i]
            for k in range(min(i + 1, max_k)):
                ans += (cur + cur_max) * comb(i, k) % MOD
            ans %= MOD

        return ans % MOD
