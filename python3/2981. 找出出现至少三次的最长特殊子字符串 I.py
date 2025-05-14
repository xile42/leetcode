class Solution:

    def maximumLength(self, s: str) -> int:

        ans = -1
        d = defaultdict(lambda: defaultdict(int))
        for c, ite in groupby(s):
            l = len(list(ite))
            for i in range(1, l + 1):
                d[c][i] += l + 1 - i
        for c in d:
            for l in d[c]:
                if d[c][l] >= 3:
                    ans = max(ans, l)

        return ans
