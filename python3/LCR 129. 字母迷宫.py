class Solution:

    success = False

    def check(self, i, j):

        result = list()
        offset = [
            [0, 1],
            [0, -1],
            [1, 0],
            [-1, 0],
        ]

        for i_offset, j_offset in offset:
            ii = i + i_offset
            jj = j + j_offset
            if 0 <= ii < self.m and 0 <= jj < self.n:
                result.append([ii, jj])

        return result

    def search(self, board, visit, word, i, j):

        if self.success:
            return

        if len(word) == 0:
            self.success = True
            return

        for idx, jdx in self.check(i, j):
            if not visit[idx][jdx] and board[idx][jdx] == word[0]:
                visit[idx][jdx] = True
                self.search(board, visit, word[1:], idx, jdx)
                visit[idx][jdx] = False

    def wordPuzzle(self, board: List[List[str]], word: str) -> bool:

        self.m, self.n = len(board), len(board[0])
        visit = [[False for _ in range(self.n)] for _ in range(self.m)]
        self.success = False
        for idx in range(self.m):
            for jdx in range(self.n):
                if not self.success and board[idx][jdx] == word[0]:
                    visit[idx][jdx] = True
                    self.search(board, visit, word[1:], idx, jdx)
                    visit[idx][jdx] = False

        return self.success
