class Solution:

    def makeTheIntegerZero(self, num1: int, num2: int) -> int:

        for k in count(1):
            x = num1 - num2 * k
            if k > x:
                return -1
            if k >= x.bit_count():
                return k
