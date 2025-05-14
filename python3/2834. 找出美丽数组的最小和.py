class Solution:

    def minimumPossibleSum(self, n: int, target: int) -> int:

        base = 10 ** 9 + 7
        m = min(target // 2, n)

        return ((m * (m + 1) + (target * 2 + n - m - 1) * (n - m)) // 2) % base
