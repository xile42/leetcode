class Solution:

    def gameOfLife(self, board: List[List[int]]) -> None:

        m, n = len(board), len(board[0])
        board_next = [[0 for _ in range(n)] for _ in range(m)]
        for idx in range(m):
            for jdx in range(n):
                live_count = 0
                for i in idx, idx+1, idx-1:
                    for j in jdx, jdx+1, jdx-1:
                        if (not (idx == i and jdx == j)) and 0 <= i < m and 0 <= j < n:
                            live_count += board[i][j]
                board_next[idx][jdx] = board[idx][jdx]
                if live_count < 2:
                    board_next[idx][jdx] = 0
                elif live_count > 3:
                    board_next[idx][jdx] = 0
                elif live_count == 3:
                    board_next[idx][jdx] = 1

        for idx in range(m):
            for jdx in range(n):
                board[idx][jdx] = board_next[idx][jdx]
