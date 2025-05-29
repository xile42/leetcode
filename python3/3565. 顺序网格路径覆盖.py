from copy import deepcopy


class Solution:

    def findPath(self, grid: List[List[int]], k: int) -> List[List[int]]:

        m, n = len(grid), len(grid[0])
        vis = [[False for _ in range(n)] for _ in range(m)]
        path = list()
        ans = None

        def dfs(i, j, limit):

            nonlocal ans
            if ans:
                return

            path.append([i, j])
            vis[i][j] = True
            for ii, jj in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                if 0 <= ii < m and 0 <= jj < n and not vis[ii][jj]:
                    if grid[ii][jj] == 0:
                        dfs(ii, jj, limit)
                    elif grid[ii][jj] == limit + 1:
                        dfs(ii, jj, limit + 1)

            if len(path) == m * n:
                ans = deepcopy(path)

            path.pop(-1)
            vis[i][j] = False

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 or grid[i][j] == 1:
                    dfs(i, j, grid[i][j])
                    if ans is not None:
                        return ans

        return list()
