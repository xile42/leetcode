class Solution:

    def insertBits(self, N: int, M: int, i: int, j: int) -> int:

        sn, sm = bin(N)[2:], bin(M)[2:]
        l = j - i + 1
        sm = "0" * (l - len(sm)) + sm
        sm = sm[-l:]
        sn = "0" * (j - len(sn)) + sn
        ans = list(sn)[::-1]
        ans[i:j + 1] = list(sm[::-1])

        return int("".join(ans[::-1]), 2)
