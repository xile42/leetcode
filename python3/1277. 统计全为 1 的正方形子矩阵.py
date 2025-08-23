class Solution:

    def countSquares(self, matrix: List[List[int]]) -> int:

        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            dp[i][0] = matrix[i][0]
        for j in range(n):
            dp[0][j] = matrix[0][j]

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    continue
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1 if i > 0 and j > 0 else 1

        return sum(sum(row) for row in dp)
