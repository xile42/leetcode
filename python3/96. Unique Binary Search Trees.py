# Given an integer n, return the number of structurally unique BST's (binary
# search trees) which has exactly n nodes of unique values from 1 to n.
#
#
#  Example 1:
#
#
# Input: n = 3
# Output: 5
#
#
#  Example 2:
#
#
# Input: n = 1
# Output: 1
#
#
#
#  Constraints:
#
#
#  1 <= n <= 19
#
#
#  Related Topics Math Dynamic Programming Tree Binary Search Tree Binary Tree ?
# ? 10408 👎 407


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def numTrees(self, n: int) -> int:

        if n == 1:
            return 1

        dp = [0 for _ in range(n+1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            for j in range(i):
                dp[i] += dp[j] * dp[i-1-j]

        return dp[-1]

# leetcode submit region end(Prohibit modification and deletion)
