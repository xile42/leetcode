# Given two integers dividend and divisor, divide two integers without using
# multiplication, division, and mod operator.
#
#  The integer division should truncate toward zero, which means losing its
# fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be
# truncated to -2.
#
#  Return the quotient after dividing dividend by divisor.
#
#  Note: Assume we are dealing with an environment that could only store
# integers within the 32-bit signed integer range: [−2³¹, 2³¹ − 1]. For this problem, if
# the quotient is strictly greater than 2³¹ - 1, then return 2³¹ - 1, and if the
# quotient is strictly less than -2³¹, then return -2³¹.
#
#
#  Example 1:
#
#
# Input: dividend = 10, divisor = 3
# Output: 3
# Explanation: 10/3 = 3.33333.. which is truncated to 3.
#
#
#  Example 2:
#
#
# Input: dividend = 7, divisor = -3
# Output: -2
# Explanation: 7/-3 = -2.33333.. which is truncated to -2.
#
#
#
#  Constraints:
#
#
#  -2³¹ <= dividend, divisor <= 2³¹ - 1
#  divisor != 0
#
#
#  Related Topics Math Bit Manipulation 👍 5207 👎 14846


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    int_max = 1 << 31

    def divide(self, dividend: int, divisor: int) -> int:

        sign = 1
        if (dividend < 0 < divisor) or (dividend > 0 > divisor):
            sign = -1
        dis = abs(divisor)
        did = abs(dividend)

        if did < dis:
            return 0

        result = 0
        while did >= dis:
            count = 0
            while did > (dis << (count+1)):
                count += 1
            did -= dis << count
            result += 1 << count

        if result == self.int_max and sign == 1:
            return self.int_max - 1

        if sign == 1:
            return result
        else:
            return -result

# leetcode submit region end(Prohibit modification and deletion)
