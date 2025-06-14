def f(n):

    mn = inf
    x, y = 0, 0
    for i in range(1, isqrt(n) + 1):
        if n % i == 0:
            j = n // i
            if abs(i - j) < mn:
                mn, x, y = abs(i - j), i, j

    return mn, x, y


class Solution:

    def closestDivisors(self, num: int) -> List[int]:

        mn1, x1, y1 = f(num + 1)
        mn2, x2, y2 = f(num + 2)

        if mn1 < mn2:
            return [x1, y1]
        else:
            return [x2, y2]
