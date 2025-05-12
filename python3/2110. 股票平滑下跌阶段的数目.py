class Solution:

    def getDescentPeriods(self, prices: List[int]) -> int:

        ns = [i + v for i, v in enumerate(prices)]
        ans = 0
        for c, ite in groupby(ns):
            l = len(list(ite))
            ans += l * (l + 1) // 2

        return ans
