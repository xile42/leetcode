class Solution:

    def orangesRotting(self, grid: List[List[int]]) -> int:

        queue = deque()
        m, n = len(grid), len(grid[0])
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    cnt += 1

        ans = 0
        while True:
            next_queue = deque()
            while queue:
                i, j = queue.popleft()
                for ii, jj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                    if 0 <= ii < m and 0 <= jj < n and grid[ii][jj] == 1:
                        grid[ii][jj] = 2
                        cnt -= 1
                        next_queue.append((ii, jj))
            if len(next_queue) == 0:
                return -1 if cnt > 0 else ans
            queue = next_queue
            ans += 1
