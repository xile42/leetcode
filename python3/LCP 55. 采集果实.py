class Solution:

    def getMinimumTime(self, time: List[int], fruits: List[List[int]], limit: int) -> int:

        ans = 0
        for i, n in fruits:
            k = ceil(n / limit)
            ans += time[i] * k

        return ans
