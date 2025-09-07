class Solution:

    def maxJump(self, stones: List[int]) -> int:

        ans = 0 if len(stones) > 2 else stones[-1] - stones[0]
        for i in range(2, len(stones)):
            ans = max(ans, stones[i] - stones[i - 2])

        return ans
