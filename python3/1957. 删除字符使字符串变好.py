class Solution:

    def makeFancyString(self, s: str) -> str:

        res = str()
        for c, ite in groupby(s):
            l = len(list(ite))
            res += c * l if l <= 2 else c * 2

        return res
