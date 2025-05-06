class Solution:

    def countBattleships(self, board: List[List[str]]) -> int:

        m, n = len(board), len(board[0])
        vis = [[False for _ in range(n)] for _ in range(m)]

        ans = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] != "X":
                    continue
                if vis[i][j]:
                    continue
                vis[i][j] = True
                ii, jj = i, j
                while jj + 1 < n and not vis[ii][jj + 1] and board[ii][jj + 1] == "X":
                    jj += 1
                    vis[ii][jj] = True
                ii, jj = i, j
                while ii + 1 < m and not vis[ii + 1][jj] and board[ii + 1][jj] == "X":
                    ii += 1
                    vis[ii][jj] = True
                ans += 1

        return ans
