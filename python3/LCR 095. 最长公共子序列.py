class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        m, n = len(text1), len(text2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

        for i in range(n+1):
            dp[0][i] = 0
        for i in range(m+1):
            dp[i][0] = 0

        for i in range(1, m+1):
            for j in range(1, n+1):
                c1, c2 = text1[i-1], text2[j-1]
                if c1 == c2:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])

        return dp[-1][-1]
