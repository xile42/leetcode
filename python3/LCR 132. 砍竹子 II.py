class Solution:

    def cuttingBamboo(self, n: int) -> int:

        base = 10 ** 9 + 7

        if n <= 3:
            return n - 1

        if n % 3 == 0:
            return 3 ** (n // 3) % base
        elif n % 3 == 1:
            return 3 ** (n // 3 - 1) * 4 % base
        else:
            return 3 ** (n // 3) * 2 % base
