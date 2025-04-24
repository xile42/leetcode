class Solution:

    def minCost(self, colors: str, neededTime: List[int]) -> int:

        left = 0
        cur = 0
        s = sum(neededTime)
        for c, ite in groupby(colors):
            l = len(list(ite))
            left += max(neededTime[cur:cur + l])
            cur += l

        return s - left
