# You are given an m x n integer matrix matrix with the following two
# properties:
#
#
#  Each row is sorted in non-decreasing order.
#  The first integer of each row is greater than the last integer of the
# previous row.
#
#
#  Given an integer target, return true if target is in matrix or false
# otherwise.
#
#  You must write a solution in O(log(m * n)) time complexity.
#
#
#  Example 1:
#
#
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
#
#
#  Example 2:
#
#
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false
#
#
#
#  Constraints:
#
#
#  m == matrix.length
#  n == matrix[i].length
#  1 <= m, n <= 100
#  -10⁴ <= matrix[i][j], target <= 10⁴
#
#
#  Related Topics Array Binary Search Matrix 👍 15922 👎 424


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def idx_transform(self, idx, n):
        i = idx // n
        j = idx % n
        return i, j

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m, n = len(matrix), len(matrix[0])
        mn = m * n

        l = 0
        r = mn-1

        if matrix[-1][-1] < target or matrix[0][0] > target:
            return False

        while l <= r:
            mid = l + (r-l) // 2
            i, j = self.idx_transform(mid, n)
            m_value = matrix[i][j]
            if m_value == target:
                return True
            if m_value < target:
                l = mid + 1
            else:
                r = mid - 1

        return False

# leetcode submit region end(Prohibit modification and deletion)
