class Solution:

    def minSideJumps(self, obstacles: List[int]) -> int:

        # n = len(obstacles)
        #
        # @cache
        # def f(pos, channel):
        #
        #     if pos >= n:
        #         return 0
        #
        #     while pos + 1 < n and obstacles[pos + 1] != channel:
        #         pos += 1
        #
        #     if pos == n - 1:
        #         return f(pos + 1, channel)
        #
        #     ans = inf
        #     for next_channel in range(1, 4):
        #         if channel != next_channel and obstacles[pos] != next_channel:
        #             ans = min(ans, f(pos + 1, next_channel) + 1)
        #
        #     return ans
        #
        # return f(0, 2)

        dp = [inf] * 4
        dp[2] = 0
        for i in range(1, len(obstacles)):
            if obstacles[i] != 0:
                pre, dp = dp, [inf] * 4
                for x in range(1, 4):
                    if x != obstacles[i] and x != obstacles[i - 1]:
                        dp[x] = min(pre[x], 1 + pre[obstacles[i]])

        return min(dp)
