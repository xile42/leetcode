class Solution:

    def minExtraChar(self, s: str, dictionary: List[str]) -> int:

        dp = [1e9 for _ in range(len(s)+1)]
        dp[0] = 0
        for idx in range(len(s)):
            for word in dictionary:
                if len(s)-idx >= len(word) and s[idx:idx+len(word)] == word:
                    dp[idx+len(word)] = min(dp[idx+len(word)], dp[idx])
            dp[idx+1] = min(dp[idx+1], dp[idx]+1)

        return dp[len(s)]
