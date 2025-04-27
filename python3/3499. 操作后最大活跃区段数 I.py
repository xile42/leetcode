class Solution:

    def maxActiveSectionsAfterTrade(self, s: str) -> int:

        s = "1" + s + "1"
        counter = Counter(s)
        cnt0 = 0
        pre = 0
        ans = 0
        for c, ite in groupby(s):
            l = len(list(ite))
            if c == "1":
                continue
            else:
                cnt0 += 1
                ans = max(ans, l + pre)
                pre = l

        if cnt0 < 2:
            return counter["1"] - 2
        else:
            return counter["1"] - 2 + ans
