class Solution:

    def stoneGame(self, piles: List[int]) -> bool:

        l = len(piles)
        dp = [[0 for _ in range(l)] for _ in range(l)]
        for i in range(l):
            dp[i][i] = piles[i]

        for i in range(l-1):
            for j in range(i+1, l):
                dp[i][j] = max(piles[i] - dp[i+1][j], piles[j] - dp[i][j-1])

        return dp[0][l-1] > 0
