class Solution:

    def longestPalindrome(self, s: str) -> int:

        c = Counter(s)
        flag = False
        result = 0
        for i in c.values():
            if i & 1:
                flag = True
                result += i - 1
            else:
                result += i

        return result if not flag else result + 1
