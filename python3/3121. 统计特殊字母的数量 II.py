class Solution:

    def numberOfSpecialChars(self, s: str) -> int:

        ans = 0
        rs = s[::-1]
        for offset in range(26):
            little = chr(ord("a") + offset)
            big = chr(ord("A") + offset)
            i = len(s) - 1 - rs.find(little)
            j = s.find(big)
            if i != -1 and j != -1 and i < j:
                ans += 1

        return ans
