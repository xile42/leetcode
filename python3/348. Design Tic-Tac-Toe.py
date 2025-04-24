from collections import defaultdict


class TicTacToe:

    def __init__(self, n: int):

        self.n = n
        self.rows = defaultdict(lambda: defaultdict(int))
        self.cols = defaultdict(lambda: defaultdict(int))
        self.diags = defaultdict(lambda: defaultdict(int))

    def move(self, row: int, col: int, player: int) -> int:

        self.rows[row][player] += 1
        self.cols[col][player] += 1
        if row == col:
            self.diags[0][player] += 1
        if row + col == self.n - 1:
            self.diags[1][player] += 1

        if self.rows[row][player] >= self.n or self.cols[col][player] >= self.n or self.diags[0][player] >= self.n or self.diags[1][player] >= self.n:
            return player
        else:
            return 0
