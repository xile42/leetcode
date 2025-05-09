# 网格图DFS模板
class Solution:

    def colorBorder(self, grid: List[List[int]], row: int, col: int, color: int) -> List[List[int]]:

        ans = deepcopy(grid)
        m, n = len(grid), len(grid[0])
        vis = [[False for _ in range(n)] for _ in range(m)]

        def dfs(i, j):

            vis[i][j] = True
            is_border = False
            for ii, jj in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                if 0 <= ii < m and 0 <= jj < n:
                    if grid[ii][jj] != grid[i][j]:
                        is_border = True
                    elif not vis[ii][jj]:
                        dfs(ii, jj)
                else:
                    is_border = True

            if is_border:
                ans[i][j] = color

        dfs(row, col)

        return ans
