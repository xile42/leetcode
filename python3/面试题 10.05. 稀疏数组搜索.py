class Solution:

    def findString(self, words: List[str], s: str) -> int:

        ls = list(accumulate([len(w) for w in words]))
        ls_change = [(v, i) for i, v in enumerate(ls) if i == 0 or ls[i] != ls[i - 1]]
        idx = "".join(words).find(s)

        if idx in [-1, 0]:
            return idx

        for i, (l, ii) in enumerate(ls_change):
            if l == idx:
                return ls_change[i + 1][1]
