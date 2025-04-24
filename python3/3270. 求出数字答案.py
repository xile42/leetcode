class Solution:

    def generateKey(self, num1: int, num2: int, num3: int) -> int:

        ans = str()
        num1, num2, num3 = map(str, [num1, num2, num3])
        for i in range(4, 0, -1):
            ans += min("0" if len(num1) < i else num1[-i], "0" if len(num2) < i else num2[-i], "0" if len(num3) < i else num3[-i])

        return int(ans)
