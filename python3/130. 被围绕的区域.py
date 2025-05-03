# 网格图DFS模板
class Solution:

    def solve(self, grid: List[List[str]]) -> None:

        ans = 0
        m, n = len(grid), len(grid[0])
        vis = [[False for _ in range(n)] for _ in range(m)]

        def dfs(i, j):

            vis[i][j] = True
            nodes = [(i, j)]
            valid = True
            for ii, jj in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                if 0 <= ii < m and 0 <= jj < n:
                    if grid[ii][jj] == "O" and not vis[ii][jj]:
                        _nodes, _valid = dfs(ii, jj)
                        valid &= _valid
                        nodes += _nodes
                else:
                    valid = False

            return nodes, valid

        to_update = list()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "O" and not vis[i][j]:
                    nodes, valid = dfs(i, j)
                    if valid:
                        to_update += nodes

        for i, j in to_update:
            grid[i][j] = "X"
