min = lambda x, y: x if x < y else y
max = lambda x, y: x if x > y else y


class Solution:

    def minCost(self, grid: List[List[int]], k: int) -> int:

        m, n = len(grid), len(grid[0])
        dp = [[[inf for _ in range(n)] for _ in range(m)] for _ in range(k + 1)]
        dp[k][- 1][- 1] = 0

        ns = list()
        for i in range(m):
            for j in range(n):
                ns.append((grid[i][j], (i, j)))
        ns.sort(key=lambda x: x[0])
        vs = [v for v, _ in ns]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 and j == n - 1:
                    continue
                right_cost = inf if j == n - 1 else dp[k][i][j + 1] + grid[i][j + 1]
                down_cost = inf if i == m - 1 else dp[k][i + 1][j] + grid[i + 1][j]
                dp[k][i][j] = min(right_cost, down_cost)

        @cache
        def search(v):

            return bisect_right(vs, v)

        for left in range(k - 1, -1, -1):

            pre_min = [inf] * len(ns)
            for idx, (v, (i, j)) in enumerate(ns):
                if idx == 0:
                    pre_min[idx] = dp[left + 1][i][j]
                else:
                    pre_min[idx] = min(pre_min[idx - 1], dp[left + 1][i][j])

            for i in range(m - 1, -1, -1):
                for j in range(n - 1, -1, -1):
                    can_jump_i = search(grid[i][j])
                    dp[left][i][j] = min(dp[left][i][j], pre_min[can_jump_i - 1])

                    if i == m - 1 and j == n - 1:
                        continue
                    right_cost = inf if j == n - 1 else dp[left][i][j + 1] + grid[i][j + 1]
                    down_cost = inf if i == m - 1 else dp[left][i + 1][j] + grid[i + 1][j]
                    dp[left][i][j] = min(min(right_cost, down_cost), dp[left][i][j])

        ans = inf
        for left in range(k, -1, -1):
            ans = min(ans, dp[left][0][0])

        search.cache_clear()

        return ans
