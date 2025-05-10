# 网格图DFS模板
class Solution:

    def hasValidPath(self, grid: List[List[int]]) -> bool:

        success = False
        m, n = len(grid), len(grid[0])
        vis = [[False for _ in range(n)] for _ in range(m)]

        def next_ij(t, i, j):

            if t == 1:
                return (i, j + 1), (i, j - 1)
            if t == 2:
                return (i + 1, j), (i - 1, j)
            if t == 3:
                return (i, j - 1), (i + 1, j)
            if t == 4:
                return (i, j + 1), (i + 1, j)
            if t == 5:
                return (i, j - 1), (i - 1, j)
            if t == 6:
                return (i, j + 1), (i - 1, j)

        def is_connected(i_offset, j_offset, t):

            if i_offset == 1:  # 向下
                return True if t in [2, 5, 6] else False
            if i_offset == -1:  # 向上
                return True if t in [2, 3, 4] else False
            if j_offset == 1:  # 向右
                return True if t in [1, 3, 5] else False
            if j_offset == -1:  # 向左
                return True if t in [1, 4, 6] else False

        def dfs(i, j):

            nonlocal success
            if i == m - 1 and j == n - 1:
                success = True
            if success:
                return

            vis[i][j] = True
            for ii, jj in next_ij(grid[i][j], i, j):
                if 0 <= ii < m and 0 <= jj < n and is_connected(ii - i, jj - j, grid[ii][jj]) and not vis[ii][jj]:
                    dfs(ii, jj)

        dfs(0, 0)

        return success
