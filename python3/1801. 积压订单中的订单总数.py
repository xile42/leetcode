class Solution:

    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:

        buy = list()
        sell = list()
        for p, a, t in orders:
            if t == 0:
                bp, ba = p, a
                while ba and sell and sell[0][0] <= bp:
                    sp, sa = heappop(sell)
                    sa, ba = max(0, sa - ba), max(0, ba - sa)
                    if sa > 0:
                        heappush(sell, [sp, sa])
                if ba > 0:
                    heappush(buy, [-bp, ba])
            else:
                sp, sa = p, a
                while sa and buy and -buy[0][0] >= sp:
                    bp, ba = heappop(buy)
                    bp = -bp
                    sa, ba = max(0, sa - ba), max(0, ba - sa)
                    if ba > 0:
                        heappush(buy, [-bp, ba])
                if sa > 0:
                    heappush(sell, [sp, sa])

        ans = 0
        base = 10 ** 9 + 7
        for p, a in buy:
            ans += a % base
            ans %= base
        for p, a in sell:
            ans += a % base
            ans %= base

        return ans % base
