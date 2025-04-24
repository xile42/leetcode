class Solution:

    @cache
    def f(self, n):

        if n == 1:
            return 0

        if n & 1:
            return self.f((n - 1) // 2 + 1) + (n - 1) // 2
        else:
            return self.f(n // 2) + n // 2

    def numberOfMatches(self, n: int) -> int:

        return self.f(n)
