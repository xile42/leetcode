class Solution:

    def partitionLabels(self, s: str) -> List[int]:

        d = dict()
        for i, c in enumerate(s):
            d[c] = i

        cur = d[s[0]]
        ans = list()
        for i, c in enumerate(s):
            cur = max(cur, d[c])
            if i == cur:
                ans.append(i)

        return [b - a for a, b in pairwise([-1] + ans)]
