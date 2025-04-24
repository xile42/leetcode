class Solution:

    def makeSmallestPalindrome(self, s: str) -> str:

        result = str()
        for i, c in enumerate(s[:len(s) // 2]):
            cc = s[-(i+1)]
            mc = min(c, cc)
            result += mc
        if len(s) & 1:
            result += s[len(s)//2]
            result += result[:-1][::-1]
        else:
            result += result[::-1]

        return result
