class Solution:

    def replaceDigits(self, s: str) -> str:

        result = str()
        for i in range(len(s)):
            if i & 1:
                result += chr(ord(s[i - 1]) + int(s[i]))
            else:
                result += s[i]

        return result
