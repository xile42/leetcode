class Solution:

    def knightDialer(self, n: int) -> int:

        offsets = [[-1, -2], [-2, -1], [-1, 2], [-2, 1], [1, -2], [1, 2], [2, -1], [2, 1]]
        base = 1000000007

        @cache
        def f(x, y, k):

            if (x == 3 and y == 0) or (x == 3 and y == 2):
                return 0

            if k == 0:
                return 1

            ans = 0
            for ox, oy in offsets:
                xx = x + ox
                yy = y + oy
                if 0 <= xx < 4 and 0 <= yy < 3:
                    ans += f(xx, yy, k - 1)
                    ans %= base

            return ans % base

        ans = 0
        for x in range(4):
            for y in range(3):
                if (x == 3 and y == 0) or (x == 3 and y == 2):
                    continue
                ans += f(x, y, n - 1)
                ans %= base

        return ans % base
