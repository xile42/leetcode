class Solution:

    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:

        t = sum(map(int, str(x)))

        return t if x % t == 0 else -1