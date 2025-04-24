# The count-and-say sequence is a sequence of digit strings defined by the
# recursive formula:
#
#
#  countAndSay(1) = "1"
#  countAndSay(n) is the run-length encoding of countAndSay(n - 1).
#
#
#  Run-length encoding (RLE) is a string compression method that works by
# replacing consecutive identical characters (repeated 2 or more times) with the
# concatenation of the character and the number marking the count of the characters (
# length of the run). For example, to compress the string "3322251" we replace "33"
# with "23", replace "222" with "32", replace "5" with "15" and replace "1" with "11
# ". Thus the compressed string becomes "23321511".
#
#  Given a positive integer n, return the nᵗʰ element of the count-and-say
# sequence.
#
#
#  Example 1:
#
#
#  Input: n = 4
#
#
#  Output: "1211"
#
#  Explanation:
#
#
# countAndSay(1) = "1"
# countAndSay(2) = RLE of "1" = "11"
# countAndSay(3) = RLE of "11" = "21"
# countAndSay(4) = RLE of "21" = "1211"
#
#
#
#  Example 2:
#
#
#  Input: n = 1
#
#
#  Output: "1"
#
#  Explanation:
#
#  This is the base case.
#
#
#  Constraints:
#
#
#  1 <= n <= 30
#
#
#
# Follow up: Could you solve it iteratively?
#
#  Related Topics String 👍 4043 👎 8367


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def count_and_say(self, base_string):

        start_idx = 0
        end_idx = 0

        result = str()
        while start_idx < len(base_string):
            while end_idx < len(base_string) - 1 and base_string[end_idx] == base_string[end_idx+1]:
                end_idx += 1

            count = end_idx - start_idx + 1
            char = base_string[start_idx]
            result += str(count) + char

            start_idx = end_idx + 1
            end_idx = start_idx

        return result

    def solve(self, n):

        if n == 1:
            return "1"

        return self.count_and_say(self.solve(n-1))

    def countAndSay(self, n: int) -> str:

        result = self.solve(n)
        return result

# leetcode submit region end(Prohibit modification and deletion)
