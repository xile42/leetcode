class Solution:

    def trainWays(self, num: int) -> int:

        base = 10 ** 9 + 7
        dp = [1, 1, 2]
        if num <= 2:
            return dp[num]
        while len(dp) < num + 1:
            dp.append((dp[-1] + dp[-2]) % base)

        return dp[num] % base