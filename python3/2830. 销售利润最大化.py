class Solution:

    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:

        d = defaultdict(list)
        for s, e, g in offers:
            d[e].append((s, g))

        dp = [0] * n
        for e in range(n):
            dp[e] = dp[e - 1] if e > 0 else 0
            for s, g in d[e]:
                if s == 0:
                    dp[e] = max(dp[e], g)
                else:
                    dp[e] = max(dp[e], dp[s - 1] + g)

        return dp[-1]
