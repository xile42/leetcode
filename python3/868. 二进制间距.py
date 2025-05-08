class Solution:

    def binaryGap(self, n: int) -> int:

        ans = 0
        cnt = 0
        pre = -inf
        for c, ite in groupby(bin(n)[2:]):
            if c == "1":
                cnt += 1
                ans = max(ans, pre)
            if c == "0" and cnt >= 1:
                pre = len(list(ite)) + 1

        return ans if cnt >= 2 else (1 if bin(n)[2:].count("1") > 1 else 0)
