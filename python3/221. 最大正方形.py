class Solution:

    def maximalSquare(self, matrix: List[List[str]]) -> int:

        m, n = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        dp[0][0] = 1 if matrix[0][0] == "1" else 0
        for i in range(1, n):
            if matrix[0][i] == "1":
                dp[0][i] = min(dp[0][i - 1] + 1, 1)
        for i in range(1, m):
            if matrix[i][0] == "1":
                dp[i][0] = min(dp[i - 1][0] + 1, 1)

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == "1":
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
                else:
                    dp[i][j] = 0

        return max([max(row) for row in dp]) ** 2
