class Solution:

    def tictactoe(self, moves: List[List[int]]) -> str:

        rows = defaultdict(lambda: defaultdict(int))
        cols = defaultdict(lambda: defaultdict(int))
        diags = defaultdict(lambda: defaultdict(int))

        player = 0
        for i, j in moves:
            rows[i][player] += 1
            cols[j][player] += 1
            if i == j:
                diags[0][player] += 1
            if i + j == 2:
                diags[1][player] += 1
            if rows[i][player] >= 3 or cols[j][player] >= 3 or diags[0][player] >= 3 or diags[1][player] >= 3:
                return "A" if player == 0 else "B"
            player = 1 - player
        if len(moves) >= 9:
            return "Draw"

        return "Pending"
