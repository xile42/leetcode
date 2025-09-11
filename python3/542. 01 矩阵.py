class Solution:

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        m, n = len(mat), len(mat[0])
        ans = [[inf for _ in range(n)] for _ in range(m)]
        q = deque()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    ans[i][j] = 0
                    q.append((i, j))

        while q:
            x, y = q.popleft()
            for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and ans[nx][ny] > ans[x][y] + 1:
                    ans[nx][ny] = ans[x][y] + 1
                    q.append((nx, ny))

        return ans
