class Solution:

    def maxScoreSightseeingPair(self, values: List[int]) -> int:

        ans = -inf
        mx = -inf
        for i, v in enumerate(values):
            if mx != -inf:
                ans = max(ans, mx + v - i)
            mx = max(mx, v + i)

        return ans
