class Solution:

    def bit_sum(self, num):

        result = 0
        while num != 0:
            result += num % 10
            num //= 10

        return result

    def addDigits(self, num: int) -> int:

        result = num
        while result >= 10:
            result = self.bit_sum(result)

        return result
