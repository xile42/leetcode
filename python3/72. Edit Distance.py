# Given two strings word1 and word2, return the minimum number of operations
# required to convert word1 to word2.
#
#  You have the following three operations permitted on a word:
#
#
#  Insert a character
#  Delete a character
#  Replace a character
#
#
#
#  Example 1:
#
#
# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation:
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
#
#
#  Example 2:
#
#
# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation:
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')
#
#
#
#  Constraints:
#
#
#  0 <= word1.length, word2.length <= 500
#  word1 and word2 consist of lowercase English letters.
#
#
#  Related Topics String Dynamic Programming 👍 14972 👎 239


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def minDistance(self, word1: str, word2: str) -> int:

        l1, l2 = len(word1), len(word2)
        dp = [[0 for _ in range(l2+1)] for _ in range(l1+1)]

        for idx in range(l1+1):
            dp[idx][0] = idx
        for idx in range(l2+1):
            dp[0][idx] = idx

        for idx in range(1, l1+1):
            for jdx in range(1, l2+1):
                if word1[idx-1] == word2[jdx-1]:
                    dp[idx][jdx] = dp[idx-1][jdx-1]
                else:
                    dp[idx][jdx] = min(dp[idx-1][jdx], dp[idx][jdx-1], dp[idx-1][jdx-1]) + 1

        return dp[l1][l2]

# leetcode submit region end(Prohibit modification and deletion)
