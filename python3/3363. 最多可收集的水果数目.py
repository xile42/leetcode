max = lambda x, y: x if x > y else y
min = lambda x, y: x if x < y else y


class Solution:

    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:

        ans = 0
        n = len(fruits)

        for i in range(n):
            ans += fruits[i][i]

        def f(fruits):

            dp = [[-inf for _ in range(n)] for _ in range(n)]
            dp[0][n - 1] = fruits[0][n - 1]
            for i in range(1, n - 1):
                for j in range(i + 1, n):
                    dp[i][j] = max(max(dp[i - 1][j], dp[i - 1][j - 1]), -inf if j == n - 1 else dp[i - 1][j + 1])
                    if dp[i][j] > -inf:
                        dp[i][j] += fruits[i][j]

            return dp[n - 2][n - 1]

        ans += f(fruits)
        ans += f(list(zip(*fruits)))

        return ans
