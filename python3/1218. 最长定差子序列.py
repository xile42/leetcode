class Solution:

    def longestSubsequence(self, arr: List[int], difference: int) -> int:

        dp = defaultdict(int)

        for n in arr:
            tar = n - difference
            dp[n] = max(dp[n], dp[tar] + 1)

        return max(dp.values())
