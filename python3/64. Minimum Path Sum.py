# Given a m x n grid filled with non-negative numbers, find a path from top
# left to bottom right, which minimizes the sum of all numbers along its path.
#
#  Note: You can only move either down or right at any point in time.
#
#
#  Example 1:
#
#
# Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
# Output: 7
# Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
#
#
#  Example 2:
#
#
# Input: grid = [[1,2,3],[4,5,6]]
# Output: 12
#
#
#
#  Constraints:
#
#
#  m == grid.length
#  n == grid[i].length
#  1 <= m, n <= 200
#  0 <= grid[i][j] <= 200
#
#
#  Related Topics Array Dynamic Programming Matrix 👍 12551 👎 172


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def minPathSum(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        dp[0][0] = grid[0][0]
        for idx in range(1, m):
            dp[idx][0] = dp[idx-1][0] + grid[idx][0]
        for idx in range(1, n):
            dp[0][idx] = dp[0][idx-1] + grid[0][idx]

        for idx in range(1, m):
            for jdx in range(1, n):
                dp[idx][jdx] = min(dp[idx-1][jdx], dp[idx][jdx-1]) + grid[idx][jdx]

        return dp[m-1][n-1]

# leetcode submit region end(Prohibit modification and deletion)
