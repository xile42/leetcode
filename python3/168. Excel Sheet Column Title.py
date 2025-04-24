class Solution:

    def convertToTitle(self, columnNumber: int) -> str:

        result = str()
        while columnNumber != 0:
            value = columnNumber % 26
            if value != 0:
                columnNumber //= 26
            else:
                if columnNumber // 26 == 1:
                    columnNumber = 0
                else:
                    columnNumber //= 26
                    columnNumber -= 1
            result += "Z" if value == 0 else chr(ord("A") + value - 1)

        return result[::-1]
