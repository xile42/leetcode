class Solution:

    def reverse(self, x: int) -> int:

        sign = -1 if x < 0 else 1
        result = int(str(abs(x))[::-1]) * sign
        if result >= pow(2, 31) or result <= -pow(2, 31):
            return 0

        return result


