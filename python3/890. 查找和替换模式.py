class Solution:

    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:

        ans = list()
        for w in words:
            d = dict()
            rd = set()
            for c1, c2 in zip(w, pattern):
                if (c1 in d and d[c1] != c2) or (c1 not in d and c2 in rd):
                    break
                d[c1] = c2
                rd.add(c2)
            else:
                ans.append(w)

        return ans
