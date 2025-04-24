class Solution:

    def checkZeroOnes(self, s: str) -> bool:

        cnt = [0, 0]
        for c, ite in groupby(s):
            l = len(list(ite))
            cnt[int(c)] = max(cnt[int(c)], l)

        return cnt[1] > cnt[0]
