class Solution:

    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:

        return sum(list(range(1, maxChoosableInteger + 1))[::-1][::2]) >= desiredTotal
