class Solution:

    def maximumLength(self, nums: List[int], k: int) -> int:

        dp = [[0 for _ in range(k)] for _ in range(k)]
        ans = 1
        for n in nums:
            n %= k
            for i in range(k):
                dp[n][i] = dp[i][n] + 1
                ans = max(ans, dp[n][i])

        return ans
