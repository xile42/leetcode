class Solution:

    def longestBeautifulSubstring(self, word: str) -> int:

        cs = list()
        ls = list()
        ans = 0
        for c, ite in groupby(word):
            cs.append(c)
            ls.append(len(list(ite)))
        for i in range(len(cs) - 4):
            if cs[i:i + 5] == ["a", "e", "i", "o", "u"]:
                ans = max(ans, sum(ls[i:i + 5]))

        return ans
