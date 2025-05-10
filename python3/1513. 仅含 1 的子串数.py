class Solution:

    def numSub(self, s: str) -> int:

        ans = 0
        base = 10 ** 9 + 7
        for c, ite in groupby(s):
            l = len(list(ite))
            if c == "1":
                ans += l * (l + 1) // 2 % base
                ans %= base

        return ans
