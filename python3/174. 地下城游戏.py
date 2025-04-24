class Solution:

    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:

        m, n = len(dungeon), len(dungeon[0])
        dp = [[-inf for _ in range(n + 1)] for _ in range(m + 1)]
        dp[m - 1][n - 1] = dungeon[m - 1][n - 1] if dungeon[m - 1][n - 1] <= 0 else 0

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 and j == n - 1:
                    continue
                v = max(dp[i + 1][j], dp[i][j + 1]) + dungeon[i][j]
                dp[i][j] = min(v, 0)

        return 1 if dp[0][0] > 0 else -(dp[0][0] - 1)
