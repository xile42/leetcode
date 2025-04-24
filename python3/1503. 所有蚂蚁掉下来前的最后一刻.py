class Solution:

    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:

        ans = 0
        for v in left:
            ans = max(ans, v)
        for v in right:
            ans = max(ans, n - v)

        return ans
