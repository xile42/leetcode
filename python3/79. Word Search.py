# Given an m x n grid of characters board and a string word, return true if
# word exists in the grid.
#
#  The word can be constructed from letters of sequentially adjacent cells,
# where adjacent cells are horizontally or vertically neighboring. The same letter
# cell may not be used more than once.
#
#
#  Example 1:
#
#
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word =
#  "ABCCED"
# Output: true
#
#
#  Example 2:
#
#
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word =
#  "SEE"
# Output: true
#
#
#  Example 3:
#
#
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word =
#  "ABCB"
# Output: false
#
#
#
#  Constraints:
#
#
#  m == board.length
#  n = board[i].length
#  1 <= m, n <= 6
#  1 <= word.length <= 15
#  board and word consists of only lowercase and uppercase English letters.
#
#
#
#  Follow up: Could you use search pruning to make your solution faster with a
# larger board?
#
#  Related Topics Array String Backtracking Matrix 👍 16009 👎 678


# leetcode submit region begin(Prohibit modification and deletion)
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

    def exist(self, board: List[List[str]], word: str) -> bool:

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

# leetcode submit region end(Prohibit modification and deletion)
