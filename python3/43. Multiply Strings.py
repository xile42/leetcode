# Given two non-negative integers num1 and num2 represented as strings, return
# the product of num1 and num2, also represented as a string.
#
#  Note: You must not use any built-in BigInteger library or convert the inputs
# to integer directly.
#
#
#  Example 1:
#  Input: num1 = "2", num2 = "3"
# Output: "6"
#
#  Example 2:
#  Input: num1 = "123", num2 = "456"
# Output: "56088"
#
#
#  Constraints:
#
#
#  1 <= num1.length, num2.length <= 200
#  num1 and num2 consist of digits only.
#  Both num1 and num2 do not contain any leading zero, except the number 0
# itself.
#
#
#  Related Topics Math String Simulation 👍 7097 👎 3366


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def multiply(self, num1: str, num2: str) -> str:

        if num1 == "0" or num2 == "0":
            return "0"

        result = 0
        for jdx in range(len(num2)-1, -1, -1):
            num2_base = pow(10, len(num2)-1-jdx)
            int_j = int(num2[jdx])
            for idx in range(len(num1)-1, -1, -1):
                num1_base = pow(10, len(num1)-1-idx)
                int_i = int(num1[idx])
                result += int_i * int_j * num1_base * num2_base

        return str(result)

# leetcode submit region end(Prohibit modification and deletion)
