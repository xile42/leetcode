class Solution:

    def maximumProfit(self, prices: List[int], k: int) -> int:

        n = len(prices)

        @cache
        def f(i, s, c):

            # s: 0 - 啥也没干  1 - 普通买入  2(0) - 普通卖出  3 - 做空卖出  4(0) - 做空买入

            if c < 0:
                return -inf

            if i == n:
                return 0 if s == 0 else -inf  # 必须完整交易

            ans = list()
            ans.append(f(i + 1, s, c))  # 跳过
            if s == 0:
                # 1
                ans.append(f(i + 1, 1, c) - prices[i])
                # 3
                ans.append(f(i + 1, 3, c) + prices[i])
            elif s == 1:
                # 2
                ans.append(f(i + 1, 0, c - 1) + prices[i])
            elif s == 3:
                # 4
                ans.append(f(i + 1, 0, c - 1) - prices[i])

            return max(ans)

        f.cache_clear()

        return f(0, 0, k)
