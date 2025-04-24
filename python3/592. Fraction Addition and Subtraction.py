# Given a string expression representing an expression of fraction addition and
# subtraction, return the calculation result in string format.
#
#  The final result should be an irreducible fraction. If your final result is
# an integer, change it to the format of a fraction that has a denominator 1. So
# in this case, 2 should be converted to 2/1.
#
#
#  Example 1:
#
#
# Input: expression = "-1/2+1/2"
# Output: "0/1"
#
#
#  Example 2:
#
#
# Input: expression = "-1/2+1/2+1/3"
# Output: "1/3"
#
#
#  Example 3:
#
#
# Input: expression = "1/3-1/2"
# Output: "-1/6"
#
#
#
#  Constraints:
#
#
#  The input string only contains '0' to '9', '/', '+' and '-'. So does the
# output.
#  Each fraction (input and output) has the format ±numerator/denominator. If
# the first input fraction or the output is positive, then '+' will be omitted.
#  The input only contains valid irreducible fractions, where the numerator and
# denominator of each fraction will always be in the range [1, 10]. If the
# denominator is 1, it means this fraction is actually an integer in a fraction format
# defined above.
#  The number of given fractions will be in the range [1, 10].
#  The numerator and denominator of the final result are guaranteed to be valid
# and in the range of 32-bit int.
#
#
#  Related Topics Math String Simulation 👍 616 👎 607


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def reduce(self, part):
        sign, up, down = part

        for num in range(2, min([up, down])):
            while up % num == 0 and down % num == 0:
                up /= num
                down /= num

        if up == 0:
            down = 1

        return sign, int(up), int(down)

    def merge(self, part_i, part_j):

        sign_i, up_i, down_i = part_i
        sign_j, up_j, down_j = part_j

        down_result = down_i * down_j
        up_i = up_i * down_j
        up_j = up_j * down_i
        if sign_i == "-":
            up_i = -up_i
        if sign_j == "-":
            up_j = -up_j
        up_result = up_i + up_j
        sign_result = "+" if up_result >= 0 else "-"
        up_result = abs(up_result)

        return [sign_result, up_result, down_result]

    def fractionAddition(self, expression: str) -> str:

        if expression[0] not in ["+", "-"]:
            expression = "+" + expression

        idx = 0
        parsed_values = list()
        while idx < len(expression):

            sign = expression[idx]
            idx += 1

            up = str()
            while expression[idx] != "/":
                up += expression[idx]
                idx += 1

            idx += 1  # "/"

            down = str()
            while idx < len(expression) and expression[idx] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                down += expression[idx]
                idx += 1

            up = int(up)
            down = int(down)
            parsed_values.append([sign, up, down])

        while len(parsed_values) != 1:
            part_i = parsed_values.pop(0)
            part_j = parsed_values.pop(0)
            part_result = self.merge(part_i, part_j)
            parsed_values.append(part_result)

        sign_result, up_result, down_result = self.reduce(parsed_values[0])


        result = str()
        if sign_result == "-":
            result += "-"
        result += "{}/{}".format(up_result, down_result)

        return result

# leetcode submit region end(Prohibit modification and deletion)
