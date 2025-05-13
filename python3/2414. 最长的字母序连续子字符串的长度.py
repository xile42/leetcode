class Solution:

    def longestContinuousSubstring(self, s: str) -> int:

        ns = [ord(c) - idx for idx, c in enumerate(s)]
        ans = 0
        for c, ite in groupby(ns):
            ans = max(ans, len(list(ite)))

        return ans
