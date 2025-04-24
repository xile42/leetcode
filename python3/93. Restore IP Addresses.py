# A valid IP address consists of exactly four integers separated by single dots.
#  Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.
#
#
#  For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011
# .255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
#
#
#  Given a string s containing only digits, return all possible valid IP
# addresses that can be formed by inserting dots into s. You are not allowed to reorder
# or remove any digits in s. You may return the valid IP addresses in any order.
#
#
#  Example 1:
#
#
# Input: s = "25525511135"
# Output: ["255.255.11.135","255.255.111.35"]
#
#
#  Example 2:
#
#
# Input: s = "0000"
# Output: ["0.0.0.0"]
#
#
#  Example 3:
#
#
# Input: s = "101023"
# Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
#
#
#
#  Constraints:
#
#
#  1 <= s.length <= 20
#  s consists of digits only.
#
#
#  Related Topics String Backtracking 👍 5264 👎 792


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    results = None

    def search(self, s, used, chance):

        if chance == 0:
            if len(s) == 0:
                self.results.append("{}.{}.{}.{}".format(*used))
            return

        if len(s) > 3 * chance or len(s) < chance:
            return

        if len(s) > 0:
            self.search(s[1:], used+[s[0]], chance-1)

        if len(s) > 1 and s[0] != "0":
            self.search(s[2:], used+[s[:2]], chance-1)

        if len(s) > 2 and s[0] != "0":
            value = int(s[:3])
            if 0 <= value <= 255:
                self.search(s[3:], used+[s[:3]], chance-1)

    def restoreIpAddresses(self, s: str) -> List[str]:

        self.results = list()
        self.search(s, list(), 4)
        return self.results

# leetcode submit region end(Prohibit modification and deletion)
