class Solution:

    def hasValidPath(self, grid: List[List[str]]) -> bool:

        if grid[0][0] == ")":
            return False

        dp = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
        m, n = len(grid), len(grid[0])

        dp[0][0][1] += 1

        for i in range(m):
            for j in range(n):
                c = grid[i][j]
                cur_v = 1 if c == "(" else -1
                if i - 1 >= 0:
                    for k, v in dp[i - 1][j].items():
                        if k + cur_v >= 0:
                            dp[i][j][k + cur_v] += v
                if j - 1 >= 0:
                    for k, v in dp[i][j - 1].items():
                        if k + cur_v >= 0:
                            dp[i][j][k + cur_v] += v

        return dp[m - 1][n - 1][0] > 0
