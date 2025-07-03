class Solution:

    def longestSquareStreak(self, nums: List[int]) -> int:

        dp = defaultdict(lambda: 1)
        nums.sort()

        for n in nums:
            dp[n] = 1

        for n in nums:
            nn = n * n
            if nn in dp:
                dp[nn] = max(dp[nn], dp[n] + 1)

        return max(dp.values()) if max(dp.values()) > 1 else -1
