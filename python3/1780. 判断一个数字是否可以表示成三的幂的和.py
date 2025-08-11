class Solution:

    def checkPowersOfThree(self, n: int) -> bool:

        def f(n, cur):

            if n == 0:
                return True

            if n < cur:
                return False

            return f(n, cur * 3) or f(n - cur, cur * 3)

        return f(n, 1)
