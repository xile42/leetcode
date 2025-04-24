class Solution:

    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:

        offsets = [[-1, -2], [-2, -1], [-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2]]
  
        @cache
        def f(x, y, t):

            if not( 0 <= x < n and 0 <= y < n ):
                return 0

            if t == 0:
                return 1

            ans = 0
            for ox, oy in offsets:
                xx, yy = x + ox, y + oy
                ans += 0 if not ( 0 <= xx < n and 0 <= yy < n ) else f(xx, yy, t - 1)

            return ans / 8

        ans = f(row, column, k)

        return ans
