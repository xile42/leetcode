# 网格图DFS模板
class Solution:

    def containsCycle(self, grid: List[List[str]]) -> bool:

        success = False
        m, n = len(grid), len(grid[0])
        vis = [[False for _ in range(n)] for _ in range(m)]

        def dfs(i, j, parent, grand_parent):

            nonlocal success
            if success:
                return
            vis[i][j] = True
            for ii, jj in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                if 0 <= ii < m and 0 <= jj < n and grid[ii][jj] == grid[i][j]:
                    if vis[ii][jj]:
                        if [ii, jj] != grand_parent and [ii, jj] != parent:
                            success = True
                            break
                    else:
                        dfs(ii, jj, [i, j], parent)

        for i in range(m):
            for j in range(n):
                if not vis[i][j]:
                    dfs(i, j, None, None)

        return success
