class Solution:

    def wardrobeFinishing(self, m: int, n: int, cnt: int) -> int:

        ans = 0
        vis = [[False for _ in range(n)] for _ in range(m)]

        def check(i, j):

            return sum(map(int, list(str(i)))) + sum(map(int, list(str(j)))) <= cnt

        def f(i, j):

            nonlocal ans
            vis[i][j] = True
            ans += 1

            for ii, jj in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                if 0 <= ii < m and 0 <= jj < n and not vis[ii][jj] and check(ii, jj):
                    f(ii, jj)

        f(0, 0)

        return ans
