# Given a positive integer n, generate an n x n matrix filled with elements
# from 1 to n² in spiral order.
#
#
#  Example 1:
#
#
# Input: n = 3
# Output: [[1,2,3],[8,9,4],[7,6,5]]
#
#
#  Example 2:
#
#
# Input: n = 1
# Output: [[1]]
#
#
#
#  Constraints:
#
#
#  1 <= n <= 20
#
#
#  Related Topics Array Matrix Simulation 👍 6427 👎 265


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def generateMatrix(self, n: int) -> List[List[int]]:

        visit = [[False for _ in range(n)] for _ in range(n)]
        result = [[0 for _ in range(n)] for _ in range(n)]
        direction = 0  # 0-r 1-d 2-l 3-u
        offsets = {
            0: [0, 1],
            1: [1, 0],
            2: [0, -1],
            3: [-1, 0],
        }

        num = 1
        count = 0
        nn = n * n
        idx = 0
        jdx = -1
        while True:
            offset_i, offset_j = offsets[direction]
            while 0 <= idx+offset_i < n and 0 <= jdx+offset_j < n and visit[idx+offset_i][jdx+offset_j] is False:
                idx += offset_i
                jdx += offset_j
                result[idx][jdx] = num
                num += 1
                count += 1
                visit[idx][jdx] = True
            if count == nn:
                break
            direction = 0 if direction == 3 else direction + 1

        return result

# leetcode submit region end(Prohibit modification and deletion)
