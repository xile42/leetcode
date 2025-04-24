class Solution:

    def titleToNumber(self, columnTitle: str) -> int:

        result = 0
        base = 1
        for char in columnTitle[::-1]:
            result += base * (ord(char) - ord("A") + 1)
            base *= 26

        return result
