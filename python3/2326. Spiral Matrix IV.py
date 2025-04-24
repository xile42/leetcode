# You are given two integers m and n, which represent the dimensions of a
# matrix.
#
#  You are also given the head of a linked list of integers.
#
#  Generate an m x n matrix that contains the integers in the linked list
# presented in spiral order (clockwise), starting from the top-left of the matrix. If
# there are remaining empty spaces, fill them with -1.
#
#  Return the generated matrix.
#
#
#  Example 1:
#
#
# Input: m = 3, n = 5, head = [3,0,2,6,8,1,7,9,4,2,5,5,0]
# Output: [[3,0,2,6,8],[5,0,-1,-1,1],[5,2,4,9,7]]
# Explanation: The diagram above shows how the values are printed in the matrix.
#
# Note that the remaining spaces in the matrix are filled with -1.
#
#
#  Example 2:
#
#
# Input: m = 1, n = 4, head = [0,1,2]
# Output: [[0,1,2,-1]]
# Explanation: The diagram above shows how the values are printed from left to
# right in the matrix.
# The last space in the matrix is set to -1.
#
#
#  Constraints:
#
#
#  1 <= m, n <= 10⁵
#  1 <= m * n <= 10⁵
#  The number of nodes in the list is in the range [1, m * n].
#  0 <= Node.val <= 1000
#
#
#  Related Topics Array Linked List Matrix Simulation 👍 784 👎 27


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:

        offsets = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        direction = 0
        results = [[None for _ in range(n)] for _ in range(m)]

        node = head
        count = 0
        x, y = 0, -1
        while count < m * n:

            dx, dy = offsets[direction]
            xx, yy = x + dx, y + dy
            while 0 <= xx < m and 0 <= yy < n and results[xx][yy] is None:
                x, y = xx, yy
                results[xx][yy] = -1 if node is None else node.val
                node = node if node is None else node.next
                xx, yy = x + dx, y + dy
                count += 1

            direction = direction + 1 if direction != 3 else 0

        return results

# leetcode submit region end(Prohibit modification and deletion)
