class Solution:

    def compressedString(self, word: str) -> str:

        ans = str()
        for c, ite in groupby(word):
            l = len(list(ite))
            while l:
                ll = min(l, 9)
                ans += "{}{}".format(ll, c)
                l -= ll

        return ans
