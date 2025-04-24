class Solution:

    def countHomogenous(self, s: str) -> int:

        ans = 0
        base = 10 ** 9 + 7
        for c, ite in groupby(s):
            l = len(list(ite))
            ans += l * (l + 1) // 2 % base
            ans %= base

        return ans
