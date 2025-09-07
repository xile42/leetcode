class Solution:

    def uniquePaths(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        dp = [[[0] * 2 for _ in range(n)] for __ in range(m)]
        dp[0][0][0] = 1
        dp[0][0][1] = 1
        base = 10 ** 9 + 7

        dp[0][1][0] = (dp[0][1][0] + 1) % base
        dp[1][0][1] = (dp[1][0][1] + 1) % base

        for i in range(m):
            for j in range(n):
                for d in range(2):

                    if i == 0 and j == 0:
                        continue
                    cur = dp[i][j][d]
                    if cur == 0:
                        continue

                    if grid[i][j] == 0:
                        if j + 1 < n:
                            dp[i][j + 1][0] = (dp[i][j + 1][0] + cur) % base
                        if i + 1 < m:
                            dp[i + 1][j][1] = (dp[i + 1][j][1] + cur) % base
                    else:
                        if d == 0:
                            if i + 1 < m:
                                dp[i + 1][j][1] = (dp[i + 1][j][1] + cur) % base
                        else:
                            if j + 1 < n:
                                dp[i][j + 1][0] = (dp[i][j + 1][0] + cur) % base

        # for row in dp:
        #     print([i[0] for i in row])
        #
        # print("---")
        #
        # for row in dp:
        #     print([i[1] for i in row])

        return (dp[m - 1][n - 1][0] + dp[m - 1][n - 1][1]) % base

        # m, n = len(grid), len(grid[0])
        # dp = [[0] * n for _ in range(m)]
        # dp[0][0] = 1
        # base = 10 ** 9 + 7
        #
        # # 刷表
        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] == 1:
        #             dp[i][j] = 0
        #         else:
        #             # 向右
        #             if j + 1 < n:
        #                 if grid[i][j + 1] == 0:  # 空格
        #                     dp[i][j + 1] = (dp[i][j + 1] + dp[i][j]) % base
        #                 else:  # 镜子
        #                     if i + 1 < m:
        #                         dp[i + 1][j + 1] = (dp[i + 1][j + 1] + dp[i][j]) % base
        #             # 向下
        #             if i + 1 < m:
        #                 if grid[i + 1][j] == 0:  # 空格
        #                     dp[i + 1][j] = (dp[i + 1][j] + dp[i][j]) % base
        #                 else:  # 镜子
        #                     if j + 1 < n:
        #                         dp[i + 1][j + 1] = (dp[i + 1][j + 1] + dp[i][j]) % base
        #
        # for row in dp:
        #     print(row)
        #
        # return dp[m - 1][n - 1] % base

        # for i in range(1, n):
        #     dp[0][i] = dp[0][i - 1] if grid[0][i] == 0 else 0
        # for j in range(1, m):
        #     dp[j][0] = dp[j - 1][0] if grid[j][0] == 0 else 0
        #
        # for i in range(1, m):
        #     for j in range(1, n):
        #         if grid[i][j] == 0:
        #             dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % base
        #         else:
        #             pass
