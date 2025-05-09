class Solution:

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        vis = [[False for _ in range(n)] for _ in range(m)]

        queue = [[0, 0]] if grid[0][0] == 0 else []
        success = False
        cnt = 0
        while queue:
            cnt += 1
            next_queue = list()
            for i, j in queue:
                if vis[i][j]:
                    continue
                if i == m - 1 and j == n - 1:
                    success = True
                    break
                vis[i][j] = True
                for ii, jj in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1), (i - 1, j - 1), (i + 1, j - 1), (i - 1, j + 1), (i + 1, j + 1):
                    if 0 <= ii < m and 0 <= jj < n and not vis[ii][jj] and grid[ii][jj] == 0:
                        next_queue.append([ii, jj])
            if success:
                break
            queue = next_queue

        return cnt if success else -1
