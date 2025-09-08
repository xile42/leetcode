class Solution:

    def solveSudoku(self, board: List[List[str]]) -> None:

        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        all_choices = set(range(1, 10))

        blanks = 0
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == '.':
                    blanks += 1
                else:
                    rows[i].add(int(board[i][j]))
                    cols[j].add(int(board[i][j]))
                    box_id = (i // 3, j // 3)
                    boxes[box_id].add(int(board[i][j]))

        def f():

            nonlocal blanks
            if blanks == 0:
                return True

            for i in range(m):
                for j in range(n):
                    if board[i][j] != '.':
                        continue

                    box_id = (i // 3, j // 3)
                    choices = all_choices - rows[i] - cols[j] - boxes[box_id]

                    for val in choices:
                        board[i][j] = str(val)
                        rows[i].add(val)
                        cols[j].add(val)
                        boxes[box_id].add(val)

                        blanks -= 1
                        if f():
                            return True

                        board[i][j] = '.'
                        rows[i].remove(val)
                        cols[j].remove(val)
                        boxes[box_id].remove(val)
                        blanks += 1

                    return False

            return False

        # 能填的先填了
        while blanks:
            before = blanks
            for i in range(m):
                for j in range(n):
                    if board[i][j] != '.':
                        continue

                    box_id = (i // 3, j // 3)
                    choices = set(range(1, 10)) - rows[i] - cols[j] - boxes[box_id]

                    if len(choices) == 1:
                        val = list(choices)[0]
                        board[i][j] = str(val)
                        rows[i].add(val)
                        cols[j].add(val)
                        boxes[box_id].add(val)
                        blanks -= 1
            if before == blanks:
                break

        # 试填法
        f()
