class Solution:

    def minimumTotal(self, triangle: List[List[int]]) -> int:

        m, n = len(triangle), len(triangle[-1])
        dp = [[inf for _ in range(n)] for _ in range(m)]
        dp[0][0] = triangle[0][0]
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + triangle[i][0]
        for row in range(1, m):
            for col in range(1, row + 1):
                dp[row][col] = min(dp[row - 1][col], dp[row - 1][col - 1]) + triangle[row][col]

        return min(dp[-1])
