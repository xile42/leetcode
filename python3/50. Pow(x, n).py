# Implement pow(x, n), which calculates x raised to the power n (i.e., xⁿ).
#
#
#  Example 1:
#
#
# Input: x = 2.00000, n = 10
# Output: 1024.00000
#
#
#  Example 2:
#
#
# Input: x = 2.10000, n = 3
# Output: 9.26100
#
#
#  Example 3:
#
#
# Input: x = 2.00000, n = -2
# Output: 0.25000
# Explanation: 2⁻² = 1/2² = 1/4 = 0.25
#
#
#
#  Constraints:
#
#
#  -100.0 < x < 100.0
#  -2³¹ <= n <= 2³¹-1
#  n is an integer.
#  Either x is not zero or n > 0.
#  -10⁴ <= xⁿ <= 10⁴
#
#
#  Related Topics Math Recursion 👍 9872 👎 9600


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def solve(self, x, n):
        if n == 0:
            return 1
        if n == 1:
            return x

        if n % 2 == 0:
            value = self.solve(x, n//2)
            return value * value
        else:
            value = self.solve(x, (n-1)//2)
            return value * value * x

    def myPow(self, x: float, n: int) -> float:

        if n == 0:
            return 1.0
        if n < 0:
            n = abs(n)
            x = 1 / x

        return float(self.solve(x, n))

# leetcode submit region end(Prohibit modification and deletion)
