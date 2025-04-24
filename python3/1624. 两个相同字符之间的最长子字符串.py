class Solution:

    def maxLengthBetweenEqualCharacters(self, s: str) -> int:

        d = defaultdict(list)
        for i, c in enumerate(s):
            d[c].append(i)

        ans = -1
        for v in d.values():
            ans = max(ans, v[-1] - v[0] - 1)

        return ans
