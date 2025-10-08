class Solution:

    def longestIdealString(self, s: str, k: int) -> int:

        n = len(s)
        dp = [[0 for _ in range(26)] for _ in range(n)]
        for i, c in enumerate(s):
            if i == 0:
                dp[i][ord(c) - ord("a")] = 1
            else:
                for j in range(26):
                    dp[i][j] = dp[i - 1][j]
                for j in range(max((ord(c) - ord("a") - k), 0), min((ord(c) - ord("a") + k), 25) + 1):
                    dp[i][ord(c) - ord("a")] = max(dp[i][ord(c) - ord("a")], dp[i - 1][j] + 1)

        return max(dp[-1])
