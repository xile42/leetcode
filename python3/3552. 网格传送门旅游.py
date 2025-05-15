class Solution:

    def minMoves(self, matrix: List[str]) -> int:

        m, n = len(matrix), len(matrix[0])
        dis = [[inf] * n for _ in range(m)]
        dis[0][0] = 0
        vis = defaultdict(lambda: False)

        pos_map = defaultdict(list)
        for i in range(m):
            for j in range(n):
                if matrix[i][j] != "." and matrix[i][j] != "#":
                    pos_map[matrix[i][j]].append((i, j))

        h = [(0, 0, 0)]
        if matrix[0][0] != "." and matrix[0][0] != "#":
            for x, y in pos_map[matrix[0][0]]:
                if x != 0 or y != 0:
                    h.append((0, x, y))

        while h:
            d, i, j = heappop(h)
            if i == m - 1 and j == n - 1:
                return d
            if d > dis[i][j]:
                continue
            for x, y in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                if 0 <= x < m and 0 <= y < n and (matrix[x][y] == "." or (matrix[x][y] != "#")):
                    new_dis = d + 1
                    if matrix[x][y] != "." and not vis[matrix[x][y]]:
                        vis[matrix[x][y]] = True
                        for xx, yy in pos_map[matrix[x][y]]:
                            if new_dis < dis[xx][yy]:  # 传送 + 不传送情况
                                dis[xx][yy] = new_dis
                                heappush(h, (new_dis, xx, yy))
                    else:
                        xx, yy = x, y
                        if new_dis < dis[xx][yy]:  # 不传送情况
                            dis[xx][yy] = new_dis
                            heappush(h, (new_dis, xx, yy))

        return -1
