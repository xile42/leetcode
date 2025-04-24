# Given two integers n and k, return all possible combinations of k numbers
# chosen from the range [1, n].
#
#  You may return the answer in any order.
#
#
#  Example 1:
#
#
# Input: n = 4, k = 2
# Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
# Explanation: There are 4 choose 2 = 6 total combinations.
# Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to
# be the same combination.
#
#
#  Example 2:
#
#
# Input: n = 1, k = 1
# Output: [[1]]
# Explanation: There is 1 choose 1 = 1 total combination.
#
#
#
#  Constraints:
#
#
#  1 <= n <= 20
#  1 <= k <= n
#
#
#  Related Topics Backtracking 👍 8284 👎 229


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    result = None

    def search(self, candidates, chance, current):

        if chance == 0:
            self.result.append(current)
            return

        for idx, num in enumerate(candidates):
            if len(candidates) - idx < chance:
                break
            self.search(candidates[idx+1:], chance-1, current+[num])

    def combine(self, n: int, k: int) -> List[List[int]]:

        self.result = list()
        self.search(list(range(1, n+1)), k, list())

        return self.result

# leetcode submit region end(Prohibit modification and deletion)
