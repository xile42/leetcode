class Solution:

    def oddString(self, words: List[str]) -> str:

        d = defaultdict(int)
        dd = dict()
        for i, w in enumerate(words):
            diff = tuple([ord(w[i + 1]) - ord(w[i]) for i in range(len(w) - 1)])
            d[diff] += 1
            dd[diff] = w
            if i >= 2:
                if d[diff] == 1:
                    return w
                if len(d) > 1:
                    for k, v in d.items():
                        if v == 1:
                            return dd[k]
