# You are given an m x n integer array grid. There is a robot initially located
# at the top-left corner (i.e., grid[0][0]). The robot tries to move to the
# bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down
# or right at any point in time.
#
#  An obstacle and space are marked as 1 or 0 respectively in grid. A path that
# the robot takes cannot include any square that is an obstacle.
#
#  Return the number of possible unique paths that the robot can take to reach
# the bottom-right corner.
#
#  The testcases are generated so that the answer will be less than or equal to
# 2 * 10⁹.
#
#
#  Example 1:
#
#
# Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# Output: 2
# Explanation: There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right
#
#
#  Example 2:
#
#
# Input: obstacleGrid = [[0,1],[0,0]]
# Output: 1
#
#
#
#  Constraints:
#
#
#  m == obstacleGrid.length
#  n == obstacleGrid[i].length
#  1 <= m, n <= 100
#  obstacleGrid[i][j] is 0 or 1.
#
#
#  Related Topics Array Dynamic Programming Matrix 👍 8817 👎 513


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
        for idx in range(1, m):
            if obstacleGrid[idx][0] == 1:
                dp[idx][0] = 0
            else:
                dp[idx][0] = dp[idx-1][0]
        for idx in range(1, n):
            if obstacleGrid[0][idx] == 1:
                dp[0][idx] = 0
            else:
                dp[0][idx] = dp[0][idx-1]

        for idx in range(1, m):
            for jdx in range(1, n):
                if obstacleGrid[idx][jdx] == 1:
                    dp[idx][jdx] = 0
                else:
                    dp[idx][jdx] = dp[idx-1][jdx] + dp[idx][jdx-1]

        return dp[m-1][n-1]
# leetcode submit region end(Prohibit modification and deletion)
