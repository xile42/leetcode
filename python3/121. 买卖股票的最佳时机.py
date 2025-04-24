class Solution:

    def maxProfit(self, prices: List[int]) -> int:

        ans = 0
        mv = prices[0]
        for v in prices[1:]:
            ans = max(ans, v - mv)
            mv = min(mv, v)

        return ans
