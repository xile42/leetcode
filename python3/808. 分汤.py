class Solution:

    def soupServings(self, n: int) -> float:

        if n >= 4451:
            return 1

        @cache
        def f(i, j):

            if i <= 0 and j <= 0:
                return 0.5
            if i <= 0:
                return 1
            if j <= 0:
                return 0

            return 0.25 * (f(i - 100, j) + f(i - 75, j - 25) + f(i - 50, j - 50) + f(i - 25, j - 75))

        return f(n, n)
