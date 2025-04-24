class Solution:

    def findLongestWord(self, s: str, dictionary: List[str]) -> str:

        def f(w):

            i = j = 0
            while i < len(s) and j < len(w):
                if s[i] == w[j]:
                    i += 1
                    j += 1
                else:
                    i += 1

            return j == len(w)

        d = defaultdict(list)
        for w in dictionary:
            if f(w):
                d[len(w)].append(w)

        if not d:
            return ""

        mx = max(d.keys())
        return min(d[mx])
