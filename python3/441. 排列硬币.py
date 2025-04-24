class Solution:

    def arrangeCoins(self, n: int) -> int:

        return max(floor((-1 + sqrt(1 + 8 * n)) / 2), 1)
