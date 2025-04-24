class Solution:

    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)

        @cache
        def dfs(i, s, f):

            if i == n - 1:
                return 0 if s == 0 else prices[i]

            ans = list()
            ans.append(dfs(i + 1, s, 0))
            if s == 1:
                ans.append(dfs(i + 1, 1 - s, 1) + prices[i])
            else:
                if f == 0:
                    ans.append(dfs(i + 1, 1 - s, f) - prices[i])

            return max(ans)

        return dfs(0, 0, 0)
