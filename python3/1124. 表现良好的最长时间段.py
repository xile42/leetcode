class Solution:

    def longestWPI(self, hours: List[int]) -> int:

        ans = 0
        s = dict()
        acc = list(accumulate([-1 if v <= 8 else 1 for v in hours]))

        for i, v in enumerate(acc):
            if v > 0:
                ans = max(ans, i + 1)
            else:
                if v - 1 in s:
                    ans = max(ans, i - s[v - 1])
            if v not in s:
                s[v] = i

        return ans
