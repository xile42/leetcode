class Solution:

    def fib(self, n: int) -> int:

        base = 10 ** 9 + 7

        @cache
        def f(i):

            return (0 if i == 0 else (1 if i == 1 else f(i - 1) + f(i - 2))) % base

        return f(n)
