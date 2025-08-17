class Solution:

    def minSensors(self, n: int, m: int, k: int) -> int:

        d = 2 * k + 1

        return ceil(n / d) * ceil(m / d)
