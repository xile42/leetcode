class Solution:

    def solve(self, x, n):
        if n == 0:
            return 1
        if n == 1:
            return x

        if n % 2 == 0:
            value = self.solve(x, n//2)
            return value * value
        else:
            value = self.solve(x, (n-1)//2)
            return value * value * x

    def myPow(self, x: float, n: int) -> float:

        if n == 0:
            return 1.0
        if n < 0:
            n = abs(n)
            x = 1 / x

        return float(self.solve(x, n))
