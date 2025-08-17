class Solution:

    def alphabetBoardPath(self, target: str) -> str:

        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        d = {c: (i, j) for i, row in enumerate(board) for j, c in enumerate(row)}

        def f(i, j, ii, jj):

            if i == ii and j == jj:
                return ""

            ans = str()
            tail = str()
            if board[i][j] == "z":
                ans += "U"
                i -= 1
            if board[ii][jj] == "z":
                tail += "D"
                ii -= 1

            if i < ii:
                ans += "D" * (ii - i)
            else:
                ans += "U" * (i - ii)
            if j < jj:
                ans += "R" * (jj - j)
            else:
                ans += "L" * (j - jj)

            return ans + tail

        ans = list()
        cur = (0, 0)
        for c in target:
            ii, jj = d[c]
            ans.append(f(cur[0], cur[1], ii, jj))
            cur = (ii, jj)

        return "!".join(ans) + "!"
