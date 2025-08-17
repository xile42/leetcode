max = lambda x, y: x if x > y else y
min = lambda x, y: x if x < y else y


class Solution:

    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:

        n = len(prices)
        ps = list(zip(prices, strategy))
        base = sum(p * s for p, s in zip(prices, strategy))

        pre = [0] * n
        pre[0] = ps[0][0] * ps[0][1]
        for i in range(1, n):
            pre[i] = pre[i - 1] + ps[i][0] * ps[i][1]

        suf = [0] * n
        suf[-1] = ps[-1][0] * ps[-1][1]
        for i in range(n - 2, -1, -1):
            suf[i] = suf[i + 1] + ps[i][0] * ps[i][1]

        left = 0
        right = k - 1
        cur = sum(prices[k // 2:k])
        ans = base
        while True:
            left_value = 0 if left == 0 else pre[left - 1]
            right_value = 0 if right == n - 1 else suf[right + 1]
            cur_value = left_value + cur + right_value
            ans = max(ans, cur_value)

            cur -= prices[left + k // 2]
            left += 1
            right += 1
            if right >= n:
                break
            cur += prices[right]

        return ans
