class Solution:

    def maxDistance(self, grid: List[List[int]]) -> int:

        n = len(grid)
        dis = [[inf for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    queue = deque()
                    queue.append([i, j, 0])
                    while queue:
                        x, y, d = queue.popleft()
                        for xx, yy in [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]]:
                            if 0 <= xx < n and 0 <= yy < n and grid[xx][yy] == 0 and dis[xx][yy] > d + 1:
                                dis[xx][yy] = d + 1
                                queue.append([xx, yy, d + 1])

        ans = -1
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0 and dis[i][j] != inf:
                    ans = max(ans, dis[i][j])

        return ans
