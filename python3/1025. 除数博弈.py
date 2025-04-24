class Solution:

    def divisorGame(self, n: int) -> bool:

        dp = [False] * (n + 1)
        if len(dp) >= 3:
            dp[2] = True
        for num in range(4, n + 1):
            for i in range(1, isqrt(num) + 1):
                if num % i == 0 and not dp[num - i]:
                    dp[num] = True
                    break

        return dp[-1]
