class Solution:

    def minArea(self, image: List[List[str]], x: int, y: int) -> int:

        m, n = len(image), len(image[0])
        x1, y1 = inf, inf
        x2, y2 = -inf, -inf
        vis = [[False for _ in range(n)] for _ in range(m)]

        def f(i, j):

            nonlocal x1, y1, x2, y2
            vis[i][j] = True
            x1 = min(x1, i)
            y1 = min(y1, j)
            x2 = max(x2, i)
            y2 = max(y2, j)
            for ii, jj in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                if 0 <= ii < m and 0 <= jj < n and not vis[ii][jj] and image[ii][jj] == "1":
                    f(ii, jj)

        f(x, y)

        return (x2 - x1 + 1) * (y2 - y1 + 1)
