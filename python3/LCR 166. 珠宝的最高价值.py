class Solution:

    def jewelleryValue(self, frame: List[List[int]]) -> int:

        m, n = len(frame), len(frame[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        dp[0][0] = frame[0][0]
        for i in range(1, n):
            dp[0][i] = frame[0][i] + dp[0][i - 1]
        for i in range(1, m):
            dp[i][0] = frame[i][0] + dp[i - 1][0]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + frame[i][j]

        return dp[-1][-1]
