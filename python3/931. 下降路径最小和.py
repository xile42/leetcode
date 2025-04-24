class Solution:

    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        n = len(matrix)
        dp = [matrix[0]] + [[inf for _ in range(n)] for _ in range(n - 1)]
        for r in range(1, n):
            for c in range(n):
                for x, y in (r - 1, c - 1), (r - 1, c), (r - 1, c + 1):
                    if 0 <= x < n and 0 <= y < n:
                        dp[r][c] = min(dp[r][c], dp[x][y] + matrix[r][c])

        return min(dp[-1])
