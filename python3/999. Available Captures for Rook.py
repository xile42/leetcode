class Solution:

    def find_first(self, values):

        for value in values:
            if value == "B":
                return 0
            elif value == "p":
                return 1

        return 0

    def numRookCaptures(self, board: List[List[str]]) -> int:

        m, n = len(board), len(board[0])
        x, y = None, None
        for i in range(m):
            for j in range(n):
                if board[i][j] == "R":
                    x, y = i, j
        row = board[x]
        col = [i[y] for i in board]

        result = 0
        result += self.find_first(row[:y][::-1])
        result += self.find_first(row[y+1:])
        result += self.find_first(col[:x][::-1])
        result += self.find_first(col[x+1:])

        return result

