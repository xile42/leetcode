# You have observations of n + m 6-sided dice rolls with each face numbered
# from 1 to 6. n of the observations went missing, and you only have the observations
# of m rolls. Fortunately, you have also calculated the average value of the n +
# m rolls.
#
#  You are given an integer array rolls of length m where rolls[i] is the value
# of the iᵗʰ observation. You are also given the two integers mean and n.
#
#  Return an array of length n containing the missing observations such that
# the average value of the n + m rolls is exactly mean. If there are multiple valid
# answers, return any of them. If no such array exists, return an empty array.
#
#  The average value of a set of k numbers is the sum of the numbers divided by
# k.
#
#  Note that mean is an integer, so the sum of the n + m rolls should be
# divisible by n + m.
#
#
#  Example 1:
#
#
# Input: rolls = [3,2,4,3], mean = 4, n = 2
# Output: [6,6]
# Explanation: The mean of all n + m rolls is (3 + 2 + 4 + 3 + 6 + 6) / 6 = 4.
#
#
#  Example 2:
#
#
# Input: rolls = [1,5,6], mean = 3, n = 4
# Output: [2,3,2,2]
# Explanation: The mean of all n + m rolls is (1 + 5 + 6 + 2 + 3 + 2 + 2) / 7 =
# 3.
#
#
#  Example 3:
#
#
# Input: rolls = [1,2,3,4], mean = 6, n = 4
# Output: []
# Explanation: It is impossible for the mean to be 6 no matter what the 4
# missing rolls are.
#
#
#
#  Constraints:
#
#
#  m == rolls.length
#  1 <= n, m <= 10⁵
#  1 <= rolls[i], mean <= 6
#
#
#  Related Topics Array Math Simulation 👍 499 👎 46


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    result = None

    def search(self, chance, target, result):  # dfs Time Limit Exceeded

        if self.result is not None:
            return

        if chance == 0 and target == 0:
            self.result = result
            return

        if target < 1 * chance or target > 6 * chance:
            return

        for roll in [1, 2, 3, 4, 5, 6]:
            self.search(chance-1, target-roll, result+[roll])

    def calculate(self, chance, need_sum):

        base_num = need_sum // chance
        base_num_plus_one_amount = need_sum % chance

        return [base_num for _ in range(chance - base_num_plus_one_amount)] + [base_num + 1 for _ in range(base_num_plus_one_amount)]

    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:

        m = len(rolls)
        current_sum = sum(rolls)
        need_sum = mean * (m + n) - current_sum

        if need_sum < 1 * n or need_sum > 6 * n:
            return list()

        # self.result = None
        # self.search(n, need_sum, list())
        #
        # if self.result is None:
        #     return list()
        #
        # return self.result

        return self.calculate(n, need_sum)

# leetcode submit region end(Prohibit modification and deletion)
