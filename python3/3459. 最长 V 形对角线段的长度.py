class Solution:

    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:

        offsets = {
            0: [-1, 1],  # 右上
            1: [1, 1],  # 右下
            2: [1, -1],  # 左下
            3: [-1, -1],  # 左上
        }

        n, m = len(grid), len(grid[0])

        @cache
        def f(x, y, d, cur, chance):

            ans = 0
            tar = 2 if cur == 1 else 2 - cur

            # 沿着方向继续走
            xx, yy = x + offsets[d][0], y + offsets[d][1]
            if 0 <= xx < n and 0 <= yy < m:
                if grid[xx][yy] == tar:
                    ans = max(ans, 1 + f(xx, yy, d, tar, chance))

            # 用机会
            if chance > 0:
                dd = (d + 1) % 4
                xx, yy = x + offsets[dd][0], y + offsets[dd][1]
                if 0 <= xx < n and 0 <= yy < m:
                    if grid[xx][yy] == tar:
                        ans = max(ans, 1 + f(xx, yy, dd, tar, chance - 1))

            return ans

        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    for d in range(4):
                        ans = max(ans, 1 + f(i, j, d, 1, 1))

        return ans
