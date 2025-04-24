class Solution:

    def findTheLongestBalancedSubstring(self, s: str) -> int:

        cnt = list()
        for c, ite in groupby(s):
            cnt.append([c, len(list(ite))])

        ans = 0
        for x, y in pairwise(cnt):
            if x[0] == "0":
                ans = max(ans, 2 * min(x[1], y[1]))

        return ans
