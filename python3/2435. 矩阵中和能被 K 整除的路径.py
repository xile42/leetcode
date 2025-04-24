class Solution:

    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:

        base = pow(10, 9) + 7
        m, n = len(grid), len(grid[0])
        dp = [[Counter() for _ in range(n)] for _ in range(m)]
        dp[0][0][grid[0][0] % k] += 1

        for i in range(1, n):
            v = grid[0][i]
            for r, cnt in dp[0][i - 1].items():
                dp[0][i][(r + v) % k] += cnt % base

        for i in range(1, m):
            v = grid[i][0]
            for r, cnt in dp[i - 1][0].items():
                dp[i][0][(r + v) % k] += cnt % base

        for i in range(1, m):
            for j in range(1, n):
                v = grid[i][j]
                for r, cnt in dp[i - 1][j].items():
                    dp[i][j][(r + v) % k] += cnt % base
                for r, cnt in dp[i][j - 1].items():
                    dp[i][j][(r + v) % k] += cnt % base

        return dp[-1][-1][0] % base
