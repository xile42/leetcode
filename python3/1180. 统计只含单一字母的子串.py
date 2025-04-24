class Solution:

    def countLetters(self, s: str) -> int:

        result = 0
        for c, ite in groupby(s):
            n = len(list(ite))
            result += n * (n + 1) // 2

        return result
