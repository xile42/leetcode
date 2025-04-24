class Solution:

    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:

        n = len(grid)
        ans = [[0 for _ in range(n)] for _ in range(n)]

        # 下
        for i in range(n):
            j = 0
            row = [grid[i][j]]
            ii = i
            jj = j
            while 0 <= (ii := ii + 1) < n and 0 <= (jj := jj + 1) < n:
                row.append(grid[ii][jj])
            row.sort(reverse=True)
            ii = i
            jj = j
            ans[ii][jj] = row[0]
            idx = 1
            while 0 <= (ii := ii + 1) < n and 0 <= (jj := jj + 1) < n:
                ans[ii][jj] = row[idx]
                idx += 1

        # 上
        for j in range(1, n):
            i = 0
            row = [grid[i][j]]
            ii = i
            jj = j
            while 0 <= (ii := ii + 1) < n and 0 <= (jj := jj + 1) < n:
                row.append(grid[ii][jj])
            row.sort()
            ii = i
            jj = j
            ans[ii][jj] = row[0]
            idx = 1
            while 0 <= (ii := ii + 1) < n and 0 <= (jj := jj + 1) < n:
                ans[ii][jj] = row[idx]
                idx += 1

        return ans
