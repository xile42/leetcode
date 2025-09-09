class Solution:

    def trapRainWater(self, heightMap: List[List[int]]) -> int:

        m, n = len(heightMap), len(heightMap[0])
        if m < 3 or n < 3:
            return 0

        vis = [[False] * n for _ in range(m)]
        heap = list()

        for i in range(m):
            for j in [0, n - 1]:
                heappush(heap, (heightMap[i][j], i, j))
                vis[i][j] = True

        for j in range(1, n - 1):
            for i in [0, m - 1]:
                heappush(heap, (heightMap[i][j], i, j))
                vis[i][j] = True

        ans = 0
        max_height = 0

        while heap:
            height, x, y = heapq.heappop(heap)
            max_height = max(max_height, height)

            for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not vis[nx][ny]:
                    if heightMap[nx][ny] < max_height:
                        ans += max_height - heightMap[nx][ny]
                    heappush(heap, (heightMap[nx][ny], nx, ny))
                    vis[nx][ny] = True

        return ans
